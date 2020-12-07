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

    seat_list = []

    in_lines = []
    with open("input.txt", 'r') as input_file:
        in_lines = input_file.readlines()

    for line in in_lines:
        seat_data = seat_part_to_row_col_id(line)
        seat_list.append(seat_data)

    highest_seat = 0
    for seat in seat_list:
        highest_seat = max(highest_seat, seat[2])

    print(f"Highest seat-id = {highest_seat}")


# Make sure main is called
main()
print("\nDone.\n")
