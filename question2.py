from dataclasses import dataclass


filename = "day2input.txt"


@dataclass
class MoveInstruction:
    direction: str
    step: int


def read_instructions(filename):
    with open(filename, "r") as file:
        for line in file:
            parts = line.split()

            direction = parts[0]
            step = int(parts[1])

            yield MoveInstruction(direction, step)


horizontal = 0
depth = 0

for instruction in read_instructions(filename):
    if instruction.direction == "forward":
        horizontal = horizontal + instruction.step
        print(f"Horizontal: {horizontal}, Depth: {depth}")

    elif instruction.direction == "down":
        depth = depth + instruction.step
        print(f"Horizontal: {horizontal}, Depth: {depth}")

    elif instruction.direction == "up":
        depth = depth - instruction.step
        print(f"Horizontal: {horizontal}, Depth: {depth}")

print(f"\nFinal Horizontal: {horizontal}, Final Depth: {depth}")