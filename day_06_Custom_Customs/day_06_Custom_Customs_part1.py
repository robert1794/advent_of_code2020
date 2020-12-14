


# Remove any duplicate characters in a string
# e.g. "abbbc" -> "abc"
def filter_unique_characters(in_string):
    out_string = ""

    for char in in_string:
        if char not in out_string:
            out_string += char

    return out_string


#  The main loop in its natural habitat
def main():

    file_entries = []
    with open("input.txt", 'r') as input_file:
        input_blob = input_file.read()
        file_entries = input_blob.split("\n\n")

    input_entries = []

    for part in file_entries:
        part_str = part.replace("\n", " ")
        input_entries.append(part_str)

    nr_unique_answers = 0

    for line in input_entries:
        short_answer = filter_unique_characters(line)
        short_answer = short_answer.replace(" ", "")
        nr_unique_answers += len(short_answer)

    print(f"Total number of unique answers per group: {nr_unique_answers}")


#  Make sure main is called
main()
print("\nDone.\n")
