

import sys
import re

# The number we are looking for in the assignment. Should be the result of number1 + number2 + number3
target_sum = 2020


def is_pwd_valid(c_first, c_second, char, pwd):
	if bool(pwd[c_first - 1] == char) ^ bool(pwd[c_second - 1] == char) :
		return True
	else:
		return False



## The main function in its natural habitat
def main():

	numbers = []

	with open("input.txt", 'r') as input_file:
		in_lines = input_file.readlines()
		cnt_valid = 0
		for line in in_lines:
			c_first, c_second, char, pwd, _ = re.split("\s|\-|:\s", line)
			if is_pwd_valid(int(c_first), int(c_second), char, pwd):
				cnt_valid += 1

		print(f"Total valid passwords: {cnt_valid}")


main()
print("\nDone.\n")
