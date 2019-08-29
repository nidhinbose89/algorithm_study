#!/usr/bin/env python

"""
Flood Fill!!

Author:nidhinbose89
"""
import pprint

input_arr = ["....................",
             ".......XXXXXXXXXX...",
             ".......X........X...",
             ".......X........X...",
             "..XXXXXX........X...",
             "..X.............X...",
             "..X.............X...",
             "..X........XXXXXX...",
             "..X........X........",
             "..XXXX..XXXX........",
             ".....XXXX...........",
             "....................",
             "....................", ]

input_arr = """
....................
.......XXXXXXXXXX...
.......X........X...
.......X........X...
..XXXXXX........X...
..X.............X...
..X.............X...
..X........XXXXXX...
..X........X........
..XXXX..XXXX........
.....XXXX...........
....................
....................
"""

if type(input_arr) == str:
    input_arr = input_arr.strip().split('\n')

max_x = len(input_arr[0])
max_y = len(input_arr)


def floodfill(surface, x, y, old_color, new_color):
    """Assume surface is a 2D image and surface[x][y] is the color at x, y."""
    if surface[x][y] != old_color or x >= max_y or y >= max_x:  # the base case
        return
    str_row = surface[x]
    modif_str = "".join((str_row[:y], new_color, str_row[y + 1:]))
    surface[x] = modif_str

    floodfill(surface, x + 1, y, old_color, new_color)  # right
    floodfill(surface, x - 1, y, old_color, new_color)  # left
    floodfill(surface, x, y + 1, old_color, new_color)  # down
    floodfill(surface, x, y - 1, old_color, new_color)  # up
    # 8 connected calls -- this will penetrate diagonally as well
    floodfill(surface, x + 1, y + 1, old_color, new_color)  # diag - quadrant 1
    floodfill(surface, x - 1, y + 1, old_color, new_color)  # diag - quadrant 2
    floodfill(surface, x - 1, y - 1, old_color, new_color)  # diag - quadrant 3
    floodfill(surface, x + 1, y - 1, old_color, new_color)  # diag - quadrant 4

    return surface


pprint.pprint(floodfill(surface=input_arr, x=3,
                        y=12, old_color='.', new_color='*'))
