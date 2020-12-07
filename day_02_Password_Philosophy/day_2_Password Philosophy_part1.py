

import sys
import re

# The number we are looking for in the assignment. Should be the result of number1 + number2
target_sum = 2020




def is_pwd_valid(c_min, c_max, char, pwd):
	char_count = pwd.count(char)
	int 
	if char_count >= c_min and char_count <= c_max:
		return True
	else:
		return False



##
def main():

	# sys.argv

	numbers = []

	with open("input.txt", 'r') as input_file:
		in_lines = input_file.readlines()
		cnt_valid = 0
		for line in in_lines:
			#line_sep = line.replace(":", "")
			#c_min, c_max, char = line.split(" ")
			#print( re.split("\s|\-|:\s", line))
			c_min, c_max, char, pwd, _ = re.split("\s|\-|:\s", line)
			print(f"min: {c_min}, max: {c_max}, char: {char}, password: {pwd}")
			if is_pwd_valid(int(c_min), int(c_max), char, pwd):
				cnt_valid += 1

		print(f"Total valid passwords: {cnt_valid}")




main()
print("\nDone.\n")
