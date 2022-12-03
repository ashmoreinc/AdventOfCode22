INPUT_FILE = "input.txt"


def parse_file() -> list:
	cals_count = []

	try:
		with open(INPUT_FILE, "r") as data:
			current_elf = []
			# Loop through the data, if there is a blank line, 
			# add the data collected to the count list (cals_count)
			# then reset the list
			# otherwise add to the data (current_elf)
			for line in data:
				if line == '\n':
					cals_count.append(current_elf)
					current_elf = []
				else:
					current_elf.append(int(line))

			# Check if the last elf was handled, the list should be empty if so
			# Add the current elf if not
			if len(current_elf) != 0:
				cals_count.append(current_elf)

	except Exception as e:
		print("File read error")
		return None

	return cals_count

def main():
	# Get the elves list
	elves = parse_file()

	# Convert list of list into list of totals
	total_cals = []
	for elf in elves:
		total_cals.append(sum(elf))

	# Part one, getting the top calorie holder
	print(f"Elf count: {len(elves)}")
	print(f"Highest Calories: {max(total_cals)}, held by elf#{total_cals.index(max(total_cals))+1}")
	print(f"Lowest Calories: {min(total_cals)}, held by elf#{total_cals.index(min(total_cals))+1}")

	# Part 2, getting the top three calories holders combined total
	total_cals = sorted(total_cals)
	top_3 = total_cals[-3:]
	top_3_total = sum(top_3)
	print(f"The top three calories carriers hold a total of {top_3_total} calories")

if __name__ == "__main__":
	main()