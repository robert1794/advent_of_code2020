

##
## Parses one line form the input file to extract which bags will go in which other ones.
##
## :param      bag_line:  The bag line as read from the input file
## :type       bag_line:  string
##
## :returns:   A list containing the bag and the bags that fit inside it
## :rtype:     List[str,str]
##
def parse_bag_line(bag_line):
    bag, bag_content_str = bag_line.split("contain")

    # Okay, the following section does look quite complicated and does a lot of things at once.
    # We should split this up to make it readable...
    # Its function is split the line into strings and makes the bag names consistent. To accomplish this it does the following:
    # - Split on comma to get separate bags
    # - Remove '.', whitespaces before or after the bag name and let everything end on "bag" (remote 's' from bags)

    if bag_content_str.strip() == "no other bags.":
        bag_contents = []
    else:
        bag_contents = [i.strip().replace(".", "").split(" ", 1)[1].replace("bags", "bag") for i in bag_content_str.split(",")]
    bag = bag.strip().replace("bags", "bag")

    return {bag: bag_contents}  # return as dict


##
## Finds all bags that fit in a specific bag recursively. So if bag C fits in
## bag B and bag B fits into A then finding all bags that fit in A should return
## B and C This is recursively, to avoid being caught in a loop we build an
## exclusion list with bags already searched.
##
## :param      bags_dict_filtered:  A list of bags excluding already searched
##                                  ones
## :type       bags_dict_filtered:  { type_description }
## :param      bag_to_check:        The bag to check
## :type       bag_to_check:        { type_description }
## :param      call_id:             The call identifier, this us useful for
##                                  debugging recursion
## :type       call_id:             { type_description }
##
## :returns:   A list of all bags that can be contained somehow in the bag we
##             investigated
## :rtype:     list[strings]
##
def find_bags_that_fit_in_bag_recursively(bags_dict_filtered, bag_to_check, call_id):

    bags_dict_filtered_next = bags_dict_filtered.copy()

    try:
        del(bags_dict_filtered_next[bag_to_check])

        bags_found = set(bags_dict_filtered[bag_to_check])

        index = 0

        for bag in bags_found:
            bags_found = bags_found.union(find_bags_that_fit_in_bag_recursively(bags_dict_filtered_next, bag, call_id + str(index)))
            index += 1
    except KeyError: 
        # The bag we want to check does not exist, maybe it is already checked. Skip for now.
        print(f"WARNING: bag {bag_to_check} does not exist in dictionary. Skipping")
        bags_found = {}

    return bags_found


##
##  The main loop in its natural habitat
##
def main():
    bag_to_fit = "shiny gold bag"

    in_lines = []
    with open("input.txt", 'r') as input_file:
        in_lines = input_file.readlines()
        for line in in_lines:
            pass

    dict_of_bags = {}
    for line in in_lines:
        bag_content = parse_bag_line(line)
        dict_of_bags.update(bag_content)

    nr_of_bags_that_fit = 0

    start_bag = list(dict_of_bags.keys())[1]

    for start_bag in dict_of_bags.keys():
        bags_that_fit = find_bags_that_fit_in_bag_recursively(dict_of_bags, start_bag, 'S')
        if bag_to_fit in bags_that_fit:
            nr_of_bags_that_fit += 1

    print(f"{nr_of_bags_that_fit} bags that fit the {bag_to_fit} somehow out of {len(dict_of_bags)} total")


#  Make sure main is called
main()
print("\nDone.\n")
