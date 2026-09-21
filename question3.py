
filename = "day1input.txt"


def count_depth_changes(filename, comparison):

    previous_depth = None
    depth_count = 0

    with open(filename, "r") as file:
        for depth in file:
            current_depth = int(depth)
            if previous_depth is not None:
                if comparison(current_depth, previous_depth):
                    depth_count += 1
            previous_depth = current_depth
    return depth_count

depth_increase_count = count_depth_changes(
    filename,
    lambda current_depth, previous_depth: current_depth > previous_depth)

depth_decrease_count = count_depth_changes(
    filename,
    lambda current_depth, previous_depth: current_depth < previous_depth)

print(f"Times of depth increases: {depth_increase_count}")
print(f"Times of depth decreases: {depth_decrease_count}")
