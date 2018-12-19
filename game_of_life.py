import numpy as np
import grid
import output
import time
import sys

def main():
	init_state = np.zeros((12,12),dtype=np.bool_)
	g = grid.Grid(init_state)
	out = output.Output(1000,600)

	while not out.query_closed():
		# update graphical frame
		out.render_frame()
		print('okay')
		# framerate
		time.sleep(1./30)
		sys.stdout.flush()
# run
main()