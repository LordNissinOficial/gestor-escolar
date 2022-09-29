import curses 

class Botao():
	def __init__(self, x, y, label, funcao=None):
		self.funcao = funcao
		self.label = label
		self.x = x
		self.y = y
		self.atributos = 0
	
	def lidarInput(self, key):
		if not (key==curses.KEY_ENTER or key==10): return
		if self.funcao:
			self.funcao()
	
	def show(self, tela, highlight):
		if highlight:
			tela.addstr(self.y, self.x, self.label, curses.A_REVERSE|self.atributos)
		else:
			tela.addstr(self.y, self.x, self.label, self.atributos)