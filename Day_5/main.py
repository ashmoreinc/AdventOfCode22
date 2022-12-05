INPUT_FILE = "input.txt"

def parse_input():
	# Read the input file and combine it into a list of 2 tuples, with 2 items of each half of the line
	output_initial_state = []
	output_moves = []
	try:
		with open(INPUT_FILE, "r") as data:
			file_section = 0

			for line in data:
				if file_section == 0:
					if line == "\n":
						# Reverse the list so that the top item is at the end of the list
						# Allows us to correctly use it as a stack
						for i, val in enumerate(output_initial_state): 
							output_initial_state[i].reverse()

						# Update to the next section on line break
						file_section = 1
					else:
						# Form the initial state
						column = 0
						column_contents = ""
						_open = False
						for index, char in enumerate(line):
							# Switch column
							if (index + 1) % 4 == 0:
								# Create lists that are missing
								if len(output_initial_state) < column + 1:
									output_initial_state.append([])

								# Add item to column, before increasing the column number
								if column_contents != "":
									output_initial_state[column].append(column_contents)
								
								# Reset the column data and increase the column index
								column += 1
								column_contents = ""
								continue

							# Dont add any contents which arent enclosed in square brackets
							if char == "[":
								_open = True
							elif char == "]":
								_open = False
							elif _open:
								column_contents += char
				else:
					# Create the move data and append it to the moves list
					move_data = line.split()
					row_data = {
						"count": int(move_data[1]),
						"from": int(move_data[3]),
						"to": int(move_data[5])
					}

					output_moves.append(row_data)
	except Exception as e:
		print("Could not read input file.")
		print(str(e))
		return None

	return output_initial_state, output_moves

def get_top_rows(state):
	"""
	Print out the top rows of the stacks
	"""
	for x in state:
		print(x[-1:][0], end="")
	print()


def output_stack(state):
	"""
	Prints the stack but horizontally for ease
	"""
	print("The stacks is horizontal, i.e. turned clockwise by 90 degrees")
	for col in state:
		for row in col:
			print(row, end=" | ")

		print()


def make_moves_crate_mover_9000(state: list, moves: list):
	"""
	Move each item from one stack to another 1 by 1
	"""
	for move in moves:
		for _ in range(move["count"]):
			crate = state[move["from"] - 1].pop()
			state[move["to"] - 1].append(crate)

	output_stack(state)
	get_top_rows(state)


def make_moves_crate_mover_9001(state: list, moves: list):
	"""
	Move chunks of each 'stack' inplace from one stack to another
	"""
	for move in moves:
		state[move["to"] - 1] += state[move["from"] - 1][-move["count"]:]
		del state[move["from"] - 1][-move["count"]:]

	output_stack(state)
	get_top_rows(state)

def main():
	initial_state, moves = parse_input()

	# Task 1
	# print("Crate mover 9000:")
	# make_moves_crate_mover_9000(initial_state, moves)

	# print("#"*80)
	# print("#"*80)

	# Task 2
	print("Crate mover 9001:")
	make_moves_crate_mover_9001(initial_state, moves)


if __name__ == "__main__":
	main()