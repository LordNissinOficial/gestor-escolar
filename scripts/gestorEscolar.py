import curses
from scripts.menu import MenuInicial

class GestorEscolar:
	def __init__(self, tela):
		self.tela = tela
		self.rodando = True
		self.menu = MenuInicial(self)
	
	def novoMenu(self, menu):
		#print(str(menu))
		self.menu = menu(self)
		self.tela.clear()
		
	def sair(self):
		self.rodando = False
		
	def lidarInput(self):
		key = self.tela.getch()

		self.menu.lidarInput(key)
				
	def show(self):
		self.menu.show(self.tela)
		self.tela.refresh()