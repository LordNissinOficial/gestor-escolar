import curses
from scripts.menu import (MenuEstudante)
from scripts.usuario import Usuario

class GestorEscolar:
	def __init__(self, tela):
		self.tela = tela
		self.rodando = True
		self.menu = MenuEstudante(self)
		self.usuarios = {"admin": Usuario("admin", "senha", "diretor", {"genero": "homen", "idade": "50"})}
		self.logarUsuario("admin", "senha")
		
	def logarUsuario(self, nome, senha):
		if nome in self.usuarios and senha==self.usuarios[nome].senha:
			self.usuario = self.usuarios[nome]
			#self.novoMenu(MenuPrincipal)
		
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
		self.tela.clear()
		self.menu.show(self.tela)
		self.tela.refresh()