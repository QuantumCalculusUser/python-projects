# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python
def dirReduc(arr):
    opposite = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    stack = []
    for direction in arr:
        if stack and opposite[direction] == stack[-1]:
            stack.pop()
        else:
            stack.append(direction)
    return stack