#  NOTE: Did receive some help on this puzzle

def main():
	puzzle_input = open("puzzle_input.txt")
	puzzle_input_list = []
	
	for line in puzzle_input:
		puzzle_input_list.append(line)
		
	puzzle_input.close()

	valid_count = 0
	
	for line in puzzle_input_list:
		words = []
		invalid_found = False
		
		for word in line.split():
			if word not in words:
				words.append(word)
			else:
				invalid_found = True
				break
		
		if not invalid_found:
			valid_count += 1
				
			
	print("Part one valid count:", valid_count)
	
	valid_count = 0
	
	for line in puzzle_input_list:
		words = []
		invalid_found = False
		
		for word in line.split():
			word = sorted(word)
			if word not in words:
				words.append(word)
			else:
				invalid_found = True
				break
		
		if not invalid_found:
			valid_count += 1
			
	
	print("Part two valid count:", valid_count)
		
	
main()
