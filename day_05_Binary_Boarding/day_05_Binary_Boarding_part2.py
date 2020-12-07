# Puzzle number 5
# See https://adventofcode.com/2020/day/5


##
## Calculates the unique seat identifier.
##
## :param      row:     The row
## :type       row:     int
## :param      column:  The column
## :type       column:  int
##
## :returns:   The unique seat identifier.
## :rtype:     int
##
def calc_unique_seat_id(row: int, column: int) -> int:
    return row * 8 + column


##
## Convert the seat parititioning number to a row and column
##
## :param      seat_part_str:  The seat part string
## :type       seat_part_str:  str
##
## :returns:   { description_of_the_return_value }
## :rtype:     list [row, col, seat_id]
##
def seat_part_to_row_col_id(seat_part_str: str) -> list:
    row_str = seat_part_str[:7]
    col_str = seat_part_str[7:]

    # convert front/back and  left/right to binary 0 and 1
    row_bin = row_str.replace('B', '1').replace('F', '0')
    col_bin = col_str.replace('R', '1').replace('L', '0')

    row     = int(row_bin, 2)
    col     = int(col_bin, 2)
    seat_id = calc_unique_seat_id(row, col)

    return row, col, seat_id


## The main loop in its natural habitat
def main():
    in_lines = []
    with open("input.txt", 'r') as input_file:
        in_lines = input_file.readlines()

    # convert all lines to unique seat ids
    unique_seat_list = []
    for line in in_lines:
        seat_data = seat_part_to_row_col_id(line)
        unique_seat_list.append(seat_data[2])

    # lets get this thing sorted (so my CDO can handle it)
    unique_seat_list.sort()

    # My seat will be the one that is not in the list but for which seat-1 and seat+1 are on the list
    for seat_id in range(1, 128 * 8):
        if seat_id in unique_seat_list and seat_id + 2 in unique_seat_list:
            if seat_id + 1 not in unique_seat_list:
                print(f"your seat number is {seat_id + 1}")


# Make sure main is called
main()
print("\nDone.\n")
