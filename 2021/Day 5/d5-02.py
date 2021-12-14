"""
Day 5 Part 2

--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?
"""

with open("d5_input.txt", "r") as input_file:
    data = input_file.readlines()

grid = {}

for line in data:
    left, right = line.split(" -> ")
    x1, y1 = map(int, left.split(","))
    x2, y2 = map(int, right.split(","))
    dx = x2 - x1
    dy = y2 - y1
    if dx:
        dx = dx // abs(dx)
    if dy:
        dy = dy // abs(dy)
    x = x1
    y = y1
    while True:
        grid[(x, y)] = grid.get((x, y), 0) + 1
        if x == x2 and y == y2:
            break
        x += dx
        y += dy


lineoverlaps = 0
for i in grid.values():
    if i > 1:
        lineoverlaps += 1

print(f"Lineoverlaps: {lineoverlaps}")
