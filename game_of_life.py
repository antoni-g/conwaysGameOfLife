import numpy as np
import grid
from graphics import *

def main():
	init_state = np.zeros((12,12),dtype=np.bool_)
	g = grid.Grid(init_state)

	win = GraphWin("My Circle", 1000, 600)
	win.getMouse() # pause for click in window
	win.close()

# run
main()