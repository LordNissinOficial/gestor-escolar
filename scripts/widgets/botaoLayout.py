import curses
from scripts.widgets.botao import Botao

class BotaoLayout:
	def __init__(self, x, y):
		self.botoes = []
		self.horizontal = False
		self.x = x
		self.y = y
		self.botaoAtual = 0

	def addBotao(self, label, funcao):
		if self.horizontal:
			if len(self.botoes):
				self.botoes.append(Botao(self.x, self.botoes[-1].y+1, label, funcao))
			else:
				self.botoes.append(Botao(self.x, self.y, label, funcao))
				self.botoes[0].highlight = True
		else:
			if len(self.botoes):
				self.botoes.append(Botao(self.botoes[-1].x+len(self.botoes[-1].label)+1, self.y, label, funcao))
			else:
				self.botoes.append(Botao(self.x, self.y, label, funcao))
				self.botoes[0].highlight = True
	
	def lidarInput(self, key):
		self.botoes[self.botaoAtual].highlight = False
		if self.horizontal:
			if key==curses.KEY_DOWN:
				self.botaoAtual = min(len(self.botoes)-1, self.botaoAtual+1)
			elif key==curses.KEY_UP:
				self.botaoAtual = max(0, self.botaoAtual-1)
		else:
			if key==curses.KEY_RIGHT:
				self.botaoAtual = min(len(self.botoes)-1, self.botaoAtual+1)
			elif key==curses.KEY_LEFT:
				self.botaoAtual = max(0, self.botaoAtual-1)
		self.botoes[self.botaoAtual].highlight = True
		
	def show(self, tela):
		for botao in self.botoes:
			botao.show(tela)