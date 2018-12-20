import numpy as np
import grid
import output
import time
import sys

def main():
	init_state = np.zeros((12,12),dtype=np.bool_)
	g = grid.Grid(init_state)
	g.current_state[3][3] = 1
	g.current_state[3][4] = 1
	g.current_state[3][5] = 1
	out = output.Output(1000,600,100,12,12)
	out.render_frame(g)

	def callback():
		out.render_frame(g)

	current_frame = 0
	while not out.query_closed():
		# wait
		time.sleep(1./.7)
		out.update_fps(current_frame)
		# process grid updates, render
		g.update_tick(callback)
		current_frame += 1
# run
main()