from graphics import *

class Output(object):
	def __init__(self,size_x,size_y):
		self.win = GraphWin("My Circle", size_x, size_y)
		c = Circle(Point(50,50), 10)
		c.draw(self.win)

	def render_frame(self):
		print('frame')
		# check to see if closing
		key = self.win.checkKey()
		print(key)
		if key == "q":
			self.win.quit

	def quit(self):
		win.close()

	def query_closed(self):
		return self.win.closed