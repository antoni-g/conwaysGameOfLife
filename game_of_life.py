import numpy as np
import grid
import structures
import output
import time
import sys

def main():
	init_state = np.zeros((12,12),dtype=np.bool_)
	g = grid.Grid(init_state)
	# blinker
	structures.blinker(g,(3,4),False)
	# toad
	g.current_state[6][6] = 1
	g.current_state[6][7] = 1
	g.current_state[6][8] = 1
	g.current_state[7][7] = 1
	g.current_state[7][8] = 1
	g.current_state[7][9] = 1
	# glider
	g.current_state[8][1] = 1
	g.current_state[9][2] = 1
	g.current_state[10][2] = 1
	g.current_state[8][3] = 1
	g.current_state[9][3] =1


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