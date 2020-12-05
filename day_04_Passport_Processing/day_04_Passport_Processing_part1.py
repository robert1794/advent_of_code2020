

import sys


# List of all expected passport fields, excluding "cid" since "nobody would mind"
essential_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] 
optional_fields  = ["cid"]



def lines_to_passports(lines):
	passport_list = []
	passport_line = ""
	for line in lines:
		if len(line.strip()) <= 1:
			passport_list.append(passport_line.strip().split(" "))
			passport_line = ""
		else:
			passport_line += line.strip() + " "

	passport_list.append(passport_line.strip().split(" "))

	return passport_list


def check_passport(passport):
	#initialize fields we need to check
	fields_to_check = essential_fields.copy()

	for field in passport:
		key = field.split(":")[0]
		if key in optional_fields:
			# ignore optional fields
			continue
		elif key in fields_to_check:
			fields_to_check.remove(key)
		else:
			return False

	if len(fields_to_check) != 0:
		return False
	else:
		return True


##
def main():

	# sys.argv

	passports = []

	with open("input.txt", 'r') as input_file:
		in_lines = input_file.readlines()
		passports = lines_to_passports(in_lines)

	with open("output.txt", 'w') as output_file:
		for line in passports:
			output_file.write(str(line) + '\n')

	valid_passport_cnt = 0
	invalid_passport_cnt = 0

	for passport in passports:
		if check_passport(passport) == True:
			valid_passport_cnt += 1
		else:
			invalid_passport_cnt += 1


	print(f"{valid_passport_cnt} valid passports of {len(passports)} total, {invalid_passport_cnt} invalid")





main()
print("\nDone.\n")
