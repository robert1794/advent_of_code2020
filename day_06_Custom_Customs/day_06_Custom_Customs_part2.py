


# Remove any duplicate characters in a string
# e.g. "abbbc" -> "abc"
def filter_unique_characters(in_string):
    out_string = ""

    for char in in_string:
        if char not in out_string:
            out_string += char

    return out_string


def find_answers_for_everyone(answers_line):
    groupanswers = answers_line.split(" ")
    answers_for_everyone = groupanswers[0].strip().replace(" ", "")

    for answers in groupanswers[1:]:
        for answer_char in answers_for_everyone:
            if answer_char not in answers:
                # print(f"test {answers_for_everyone} - {answer_char}")
                answers_for_everyone = answers_for_everyone.replace(answer_char, "")
                # print(f"test {answers_for_everyone}")

    return answers_for_everyone



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

    nr_answers_by_everyone = 0

    for line in input_entries:
        answers_for_everyone = find_answers_for_everyone(line)
        nr_answers_by_everyone += len(answers_for_everyone)
        print(f"{sorted(answers_for_everyone)}, {len(answers_for_everyone)}")

    print(f"Total number of unique answers by everyone in group: {nr_answers_by_everyone}")


#  Make sure main is called
main()
print("\nDone.\n")
