

tree = '#'
road = '.'

trajectories_to_check = [[1,1], [3,1], [5,1], [7,1], [1,2]]


def calc_trees_for_trajectory(map_segment, trajectory):
    trees_bumped = 0
    dx = trajectory[0]
    dy = trajectory[1]
    x_pos = 0
    segment_width = len(map_segment[0].strip())

    for y in range(0, len(map_segment), dy):
        line = map_segment[y]
        segment_x = x_pos % segment_width
        if line[segment_x] == tree:
            trees_bumped += 1
        x_pos += dx

    return trees_bumped



# The main function in its natural habitat
def main():
    lines = []
    with open("input.txt", 'r') as input_file:
        lines = input_file.readlines()

    trees_bumped_prod = 1

    for trajectory in trajectories_to_check:
        trees_bumped = calc_trees_for_trajectory(lines, trajectory)
        trees_bumped_prod *= trees_bumped
        print(f"dx = {trajectory[0]}, dy = {trajectory[1]}, trees = {trees_bumped}")

    print(f"Product of all encountered trees = {trees_bumped_prod}")




main()
print("\nDone.\n")
