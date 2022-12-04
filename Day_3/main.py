INPUT_FILE = "input.txt"

# Letter priorities
PRIORITIES = {
	"a": 1, "b": 2,
	"c": 3, "d": 4,
	"e": 5, "f": 6,
	"g": 7, "h": 8,
	"i": 9, "j": 10,
	"k": 11, "l": 12,
	"m": 13, "n": 14,
	"o": 15, "p": 16,
	"q": 17, "r": 18,
	"s": 19, "t": 20,
	"u": 21, "v": 22,
	"w": 23, "x": 24,
	"y": 25, "z": 26,

	"A": 27, "B": 28,
	"C": 29, "D": 30,
	"E": 31, "F": 32,
	"G": 33, "H": 34,
	"I": 35, "J": 36,
	"K": 37, "L": 38,
	"M": 39, "N": 40,
	"O": 41, "P": 42,
	"Q": 43, "R": 44,
	"S": 45, "T": 46,
	"U": 47, "V": 48,
	"W": 49, "X": 50,
	"Y": 51, "Z": 52,
}

# How each group is spaced.
GROUP_STEP = 3


def parse_input():
	# Read the input file and combine it into a list of 2 tuples, with 2 items of each half of the line
	output = []
	try:
		with open(INPUT_FILE, "r") as data:
			for line in data:
				line = line.replace("\n", "")
				cont = line[:len(line)//2], line[len(line)//2:]
				output.append(cont)

	except Exception as e:
		print("Could not read input file.")
		return None

	return output


def get_missplaced_item(list1, list2):
	# Get common items between2 lists
	duplicates = list(set(list1).intersection(list2))
	return duplicates[0]


def get_common(container1, container2, container3):
	# Find common items between 3 lists/strings
	common1 = list(set(container1).intersection(container2))
	common2 = list(set(common1).intersection(container3))

	return common2[0]


def count_missplaced_priorities(containers):
	total_priority = 0

	# Loop through all ruck sacks
	# Check for the items that appear in both compartments
	# Add the priority of the item in both, to the total_priority
	for compartment1, compartment2 in containers:
		missplaced = get_missplaced_item(compartment1, compartment2)
		priority = PRIORITIES[missplaced]
		total_priority += priority

	print(f"Total priority: {total_priority}")


def count_group_priorities(containers):
	total_priority = 0

	# Loop through every 3 indexes, starting at the 3rd index
	# Then add get the common items between the item at the current index
	# and the 2 prior
	# Add the priority of the common item to the total priorities list
	for index in range(2, len(containers), GROUP_STEP):

		rucksack = containers[index][0] + containers[index][1]
		rucksack_1 = containers[index-1][0] + containers[index-1][1]
		rucksack_2 = containers[index-2][0] + containers[index-2][1]

		group_common = get_common(rucksack, rucksack_1, rucksack_2)
		
		total_priority += PRIORITIES[group_common]		
	

	print(f"Total group priority: {total_priority}")


def main():
	out = parse_input()

	if out is None:
		print("Exitting due to read failure")

	count_missplaced_priorities(out)
	count_group_priorities(out)


if __name__ == "__main__":
	main()