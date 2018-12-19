import numpy as np

class Grid(object):
	# initialize an empty game grid
	# params:
	# @ init_state - 2d np array, dtype=np.bool_
	def __init__(self,init_state):
		self.max_x = len(init_state[0])
		self.max_y = len(init_state)
		self.current_state = np.zeros((self.max_y,self.max_x),dtype=np.bool_)
		self.next_state = np.zeros((self.max_y,self.max_x),dtype=np.bool_)

	# sum the neighbors of a cell
	# assume screen edges are dead
	# params:
	# @ x - int
	# @ y - int
	def cell_neighbors(self,x,y):
		sum = 0
		left = x > 0
		top = y > 0
		right = x < self.max_x
		bottom = y < self.max_y
		if top and left:
			sum += self.current_state[y-1][x-1]
		if top:
			sum += self.current_state[y-1][x]
		if top and right:
			sum += self.current_state[y-1][x+1]
		if left:
			sum += self.current_state[y][x-1]
		if right: 
			sum += self.current_state[y][x+1]
		if left and bottom:
			sum += self.current_state[y+1][x-1]
		if bottom:
			sum += self.current_state[y+1][x]
		if bottom and right:
			sum += self.current_state[y+1][x+1]
		return sum

	# do one tick of updates on all cells, simultaneously
	def update_tick(self):
		for y in range(self.max_y):
			for x in range(self.max_x):
				res = self.cell_neighbors(x,y)
				# process game rules
				# live cells
				if self.current_state[y][x]:
					if res < 2:
						# die due to underpopulation
						self.next_state[y][x] = 0
					if res > 3:
						# die due to overpopulation
						self.next_state[y][x] = 0
				else:
					if res == 3:
						self.next_state[y][x] = 1
		# flush update into next state
		current_state = next_state
		next_state = np.zeros((self.max_y,self.max_x),dtype=np.bool_)