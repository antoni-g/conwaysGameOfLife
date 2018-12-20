import grid
import numpy as np

# creates a blinker on center, optionally vertical
# params:
# @ grid instance
# @ center of blinker - tuple(x,y)
# @ vertical indicator - boolean
def blinker(input_grid,center,vertical):
	_general_bounds_check(input_grid,center)
	# todo - properly error check
	input_grid.current_state[center[1]][center[0]] = 1
	if vertical:
		input_grid.current_state[center[1]+1][center[0]] = 1
		input_grid.current_state[center[1]-1][center[0]] = 1
	else:
		input_grid.current_state[center[1]][center[0]-1] = 1
		input_grid.current_state[center[1]][center[0]+1] = 1

def toad(input_grid,center,vertical):
	_general_bounds_check(input_grid,center)
	# todo - properly error check
	input_grid.current_state[center[1]][center[0]] = 1
	input_grid.current_state[center[1]][center[0]+1] = 1
	input_grid.current_state[center[1]+1][center[0]] = 1
	input_grid.current_state[center[1]+1][center[0]+1] = 1
	if vertical:
		input_grid.current_state[center[1]-1][center[0]+1] = 1
		input_grid.current_state[center[1]+2][center[0]] = 1
	else:
		input_grid.current_state[center[1]][center[0]-1] = 1
		input_grid.current_state[center[1]+1][center[0]+2] = 1

def glider(input_grid,center,up,left):
	_general_bounds_check(input_grid,center)
	# todo proper error checking
	if up and left:
		pass
	if up:
		pass
	if left:
		pass
	else:
		input_grid.current_state[center[1]][center[0]] = 1
		input_grid.current_state[center[1]+1][center[0]+1] = 1
		input_grid.current_state[center[1]+2][center[0]+1] = 1
		input_grid.current_state[center[1]][center[0]+2] = 1
		input_grid.current_state[center[1]+1][center[0]+2] = 1

# reusable error basic error check for grid bounds
def _general_bounds_check(grid,center):
	if center[0]<0 or center[1]<0 or center[0]>=grid.max_x or center[1]>=grid.max_y:
		raise ValueError("Attempting to place a lifeform off of the screen")