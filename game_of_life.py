import numpy as np
import grid
import output
import time
import sys

def main():
	init_state = np.zeros((12,12),dtype=np.bool_)
	g = grid.Grid(init_state)
	out = output.Output(1000,600,100,12,12)

	current_frame = 0
	while not out.query_closed():
		out.update_fps(current_frame)
		# update graphical frame
		out.render_frame(g)
		# framerate
		time.sleep(1./1)
		current_frame += 1
		sys.stdout.flush()
# run
main()