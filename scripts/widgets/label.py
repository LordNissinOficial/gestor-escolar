import curses

class Label:
	def __init__(self, x, y, label, atributos=0):
		self.x = x
		self.y = y
		self.label = label
		self.atributos = atributos
	
	def show(self, tela):
		tela.addstr(self.y, self.x, self.label, self.atributos)