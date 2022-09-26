import curses 

class Botao():
	def __init__(self, x, y, label, funcao):
		self.label = label
		self.x = x
		self.y = y
		self.highlight = False
		self.atributos = 0
	
	def usar(self):
		if self.funcao:
			self.funcao()
	
	def show(self, tela):
		if self.highlight:
			tela.addstr(self.y, self.x, self.label, curses.A_REVERSE|self.atributos)
		else:
			tela.addstr(self.y, self.x, self.label, self.atributos)