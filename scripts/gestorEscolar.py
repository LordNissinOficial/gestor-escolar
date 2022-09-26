import curses
from scripts.menu import MenuTeste

class GestorEscolar:
	def __init__(self, tela):
		self.tela = tela
		self.rodando = True
		self.menu = MenuTeste(self)
		self.menu.opcoes = ["entrar", "sair"]
	
	def novoMenu(self, menu):
		self.menu = menu(self)
		self.tela.clear()
		
	def sair(self):
		self.rodando = False
		
	def lidarInput(self):
		key = self.tela.getch()
		if key==ord("q"):
			self.sair()
		else:#key in [curses.KEY_DOWN, curses.KEY_UP, curses.KEY_ENTER, 10]:
			self.menu.lidarInput(key)
				
	def show(self):
		self.menu.show(self.tela)
		self.tela.refresh()