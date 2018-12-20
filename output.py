from graphics import *
import numpy as np
import grid

class Output(object):
	def __init__(self,size_x,size_y,offset,grid_x,grid_y):
		self.win = GraphWin("Conway's Game of Life", size_x, size_y,autoflush=False)
		# figure out grid positioning
		self.grid_x = grid_x
		self.grid_y = grid_y
		# figure out grid size
		cell_x = size_x - ((2*offset))//grid_x 
		cell_y = size_y - ((2*offset))//grid_y
		self.cell_size = min(cell_x,cell_y)
		if self.cell_size < 1:
			self.win.close()
			raise ValueError("Input window size and offset are improperly set")
		self.init_x = init_x = self.win.width//2-(self.grid_x/2)*self.cell_size
		self.init_y = offset

		print('initial: ' + str(self.init_x,self.init_y))

		# finally, init screen
		self.clear_screen()

	def clear_screen(self):
		for item in self.win.items[:]:
			item.undraw()
		for i in range(self.grid_x):
			for j in range(self.grid_y):
				curr_x = self.init_x+i*self.cell_size
				curr_y = self.init_y+i*self.cell_size
				r = Rectangle(Point(curr_x,curr_y),Point((curr_x+self.cell_size),(curr_y+self.cell_size)))
				print('drawing rect at: ' + str((curr_x,curr_y)))
				r.draw(self.win)

	def render_frame(self,grid):
		self.clear_screen()
		# draw grid
		data = grid.current_state
		for i in range(self.grid_x):
			for j in range(self.grid_y):
				if data[j][i]:
					curr_x = self.init_x+i*self.cell_size
					curr_y = self.init_y+i*self.cell_size
					r = Rectangle(curr_x,curr_y,curr_x+self.cell_size,curr_y+self.cell_size)
					r.draw(self.win)
		self.win.update()


		# check to see if closing
		key = self.win.checkKey()
		print(key)
		if key == 'q':
			self.win.close()

	def update_fps(self,fps):
		t = Text(Point(50, 50),str(fps))
		t.draw(self.win)
		self.win.update()

	def quit(self):
		win.close()

	def query_closed(self):
		return self.win.isClosed()