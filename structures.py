import grid
import numpy as np

# creates a blinker on center, optionally vertical
# params:
# @ grid instance
# @ center of blinker - tuple(x,y)
# @ vertical indicator - boolean
def blinker(grid,center,vertical):
	_general_bounds_check(grid,center)
	# todo - properly error check
	grid.current_state[center[1]][center[0]] = 1
	if vertical:
		grid.current_state[center[1]+1][center[0]] = 1
		grid.current_state[center[1]-1][center[0]] = 1
	else:
		grid.current_state[center[1]][center[0]-1] = 1
		grid.current_state[center[1]][center[0]+1] = 1

# reusable error basic error check for grid bounds
def _general_bounds_check(grid,center):
	if center[0]<0 or center[1]<0 or center[0]>=grid.max_x or center[1]>=grid.max_y:
		raise ValueError("Attempting to place a lifeform off of the screen")