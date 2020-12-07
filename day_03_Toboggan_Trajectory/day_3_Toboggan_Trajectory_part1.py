

tree = '#'
road = '.'

# The main function in its natural habitat
def main():
	lines = []
	with open("input.txt", 'r') as input_file:
		lines = input_file.readlines()

	trajectory = [3, 1] # format: delta-x, delta-y
	segment_width = len(lines[0]) -1
	position = [0,0] # left top = 0, 0

	trees_encountered = 0
	for line in lines:
		# Lets cut some corners and assume that we always go exactly 1 position down
		x_in_segment = position[0] % segment_width
		if(line[x_in_segment] == tree):
			trees_encountered += 1
		#print(position)
			print(f"{line[0:x_in_segment]}X{line[x_in_segment + 1:-1]}")
		else:
			print(f"{line[0:x_in_segment]}O{line[x_in_segment + 1:-1]}")
		position = position[0] + trajectory[0], position[1] + trajectory[1]

	print(f"Total number of trees: {trees_encountered}")







main()
print("\nDone.\n")
