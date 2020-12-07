

import sys

# The number we are looking for in the assignment. Should be the result of number1 + number2
target_sum = 2020

##
def main():

	# sys.argv

	numbers = []

	with open("input.txt", 'r') as input_file:
		in_lines = input_file.readlines()
		for line in in_lines:
			nr = int(line)
			numbers.append(nr)


	# Note the -1 is because in the last step we don't need to compare the last element with itself
	for i in range(0, len(numbers) - 1):
		# This one does go to the end to compare the number before the last with the last
		for j in range(i + 1, len(numbers)):
			number1, number2 = numbers[i], numbers[j]
			summ  = number1 + number2
			prod = number1 * number2
			if (summ == target_sum):
				print(f"Found the numbers: They are {number1} and {number2}. Sum = {summ}, product = {prod}")

	


main()
print("\nDone.\n")
