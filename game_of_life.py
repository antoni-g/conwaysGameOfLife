import numpy as np
import grid
import structures
import output
import time
import sys

def main():
	init_state = np.zeros((20,20),dtype=np.bool_)
	g = grid.Grid(init_state)
	# blinker
	structures.blinker(g,(3,4),True)
	# toad
	structures.toad(g,(8,6),True)
	# glider
	structures.glider(g,(3,10),False,False)


	out = output.Output(g,800,600,100)
	out.render_frame(g)

	def callback():
		out.render_frame(g)

	current_frame = 0
	while not out.query_closed():
		# wait
		time.sleep(1./3)
		out.update_fps(current_frame)
		# process grid updates, render
		g.update_tick(callback)
		current_frame += 1
# run
main()