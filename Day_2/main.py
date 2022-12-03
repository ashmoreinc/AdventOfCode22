# Constants for ease of use
INPUT_FILE = "input.txt"

ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"

WIN = "WIN"
LOSE = "LOSE"
DRAW = "DRAW"

# The scores added for each case
LOSS_SCORE = 0
DRAW_SCORE = 3
WIN_SCORE = 6

# Each score for the turn taken
TURN_SCORES = {
	ROCK: 1,
	PAPER: 2,
	SCISSORS: 3
}

# How each encoding maps to a turn
MAPPINGS = {
	"A": ROCK,
	"B": PAPER,
	"C": SCISSORS,
	"X": ROCK,
	"Y": PAPER,
	"Z": SCISSORS
}

# Part 2 means that x, y, z actually correspond to _how_ the game should end, not the turn
OUTCOME_MAPPINGS = {
	"X": LOSE,
	"Y": DRAW,
	"Z": WIN
}

# Order is key: player, value: oppenent
WIN_CASES = { 
	ROCK: SCISSORS,
	SCISSORS: PAPER,
	PAPER: ROCK
}

LOSE_CASES = { 
	SCISSORS: ROCK,
	PAPER: SCISSORS,
	ROCK: PAPER
}

def parse_input():
	# Loops through the input file and returns a list of lists of the turns to take
	output = []
	try:
		with open(INPUT_FILE, "r") as data:
			for line in data:
				line = line.replace("\n", "")
				output.append(line.split())

	except Exception as e:
		print("Could not read input file.")
		return None

	return output


def get_score(p1_move, p2_move):
	""" 
	Calculates and returns the score of player 1's move (p1_move) for a given turn
	"""
	if p1_move not in MAPPINGS.values():
		p1_move = MAPPINGS[p1_move]
	if p2_move not in MAPPINGS.values():
		p2_move = MAPPINGS[p2_move]


	# Calculate score
	if WIN_CASES[p1_move] == p2_move:
		# Win Case
		return TURN_SCORES[p1_move] + WIN_SCORE
	elif p1_move == p2_move:
		# Draw Case
		return TURN_SCORES[p1_move] + DRAW_SCORE

	# Lose case
	return TURN_SCORES[p1_move] + LOSS_SCORE 


def calculate_score_incorrect_encoding(turns):
	"""
	This calculates the score assuming the encoding means [opponents turn, player turn]
	"""
	
	# Calculate total score
	total_score = 0
	for turn in turns:
		opp = turn[0]
		player = turn[1]

		score = get_score(player, opp)

		total_score += score

	print(f"Total score when tracking moves would be: {total_score}")

def calculate_score_correct_encoding(turns):
	"""
	This calculates the score assuming the encoding means [oppenents turn, game outcome]
	"""
	total_score = 0
	for turn in turns:
		opp = turn[0]
		outcome = turn[1]

		if OUTCOME_MAPPINGS[outcome] == WIN:
			# Opp must lose
			player_turn = LOSE_CASES[MAPPINGS[opp]]
		elif OUTCOME_MAPPINGS[outcome] == DRAW:
			# Draw outcome
			player_turn = opp
		else:
			# Player must lose
			player_turn = WIN_CASES[MAPPINGS[opp]]

		score  = get_score(player_turn, opp)
		total_score += score

	print(f"Total score when tracking outcomes would be: {total_score}")


def main():
	out = parse_input()

	if out is None:
		print("Exitting due to failure")
		return


	calculate_score_correct_encoding(out)
	calculate_score_incorrect_encoding(out)



if __name__ == "__main__":
	main()