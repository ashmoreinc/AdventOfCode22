INPUT_FILE = "input.txt"

def parse_input():
	# Read the input file and combine it into a list of 2 tuples, with 2 items of each half of the line
	output = []
	try:
		with open(INPUT_FILE, "r") as data:
			for line in data:
				line = line.replace("\n", "")
				sections = line.split(",")
				sect1 = tuple(sections[0].split("-"))
				sect2 = tuple(sections[1].split("-"))
				output.append((sect1, sect2))

	except Exception as e:
		print("Could not read input file.")
		print(str(e))
		return None

	return output


def check_for_complete_overlaps(section_data):

	complete_overlaps = 0

	for (s1_start, s1_end), (s2_start, s2_end) in section_data:
		# Convert to ints as they come as strings
		s1_start = int(s1_start)
		s1_end = int(s1_end)
		s2_start = int(s2_start)
		s2_end = int(s2_end)

		# Check if section 2 is completely contained within section 1
		if s2_start >= s1_start and s2_start <= s1_end and \
			s2_end >= s1_start and s2_end <= s1_end:
			complete_overlaps += 1

			continue # To avoid double counting these sections

		# Check if section 1 is completely contained within section 2
		if s1_start >= s2_start and s1_start <= s2_end and \
			s1_end >= s2_start and s1_end <= s2_end:
			complete_overlaps += 1

	print(complete_overlaps)


def check_for_partial_overlaps(section_data):
	# The only difference between this and the complete overlap section is that this uses an OR comparison, rather than AND
	# Therefore it can probably be optimised to reduce the bloat. But it works so...

	complete_overlaps = 0

	for (s1_start, s1_end), (s2_start, s2_end) in section_data:
		# Convert to ints as they come as strings
		s1_start = int(s1_start)
		s1_end = int(s1_end)
		s2_start = int(s2_start)
		s2_end = int(s2_end)

		# Check if section 2 is completely contained within section 1
		if s2_start >= s1_start and s2_start <= s1_end or \
			s2_end >= s1_start and s2_end <= s1_end:
			complete_overlaps += 1

			continue # To avoid double counting these sections

		# Check if section 1 is completely contained within section 2
		if s1_start >= s2_start and s1_start <= s2_end or \
			s1_end >= s2_start and s1_end <= s2_end:
			complete_overlaps += 1

	print(complete_overlaps)

def main():
	data = parse_input()

	if data is None:
		print("Could not read input file. Exitting")
		return

	check_for_complete_overlaps(data)
	check_for_partial_overlaps(data)

if __name__ == "__main__":
	main()