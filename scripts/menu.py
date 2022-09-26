import curses
from scripts.widgets.botaoLayout import BotaoLayout

class Menu:
	def __init__(self, gestorEscolar):
		self.gestorEscolar = gestorEscolar
		self.widgets = []
		self.widgetAtual = 0
	
	def lidarInput(self, key):
		self.widgets[self.widgetAtual].lidarInput(key)
#		if key==curses.KEY_DOWN:
#			self.highlight = min(len(self.opcoes)-1, self.highlight+1)
#		elif key==curses.KEY_UP:
#			self.highlight = max(0, self.highlight-1)
#		elif key==curses.KEY_ENTER or key==10:
#			self.funcoes[self.highlight]()
	
	def showWidgets(self, tela):
		for widget in self.widgets:
			widget.show(tela)
#		else:
#			print(curses.KEY_ENTER, key)
			
#	def showOpcoes(self, tela):
#		for i, opcao in enumerate(self.opcoes):
#			if i==self.highlight:
#				tela.addstr(i, 2, opcao, curses.A_REVERSE)
#			else:
#				tela.addstr(i, 2, opcao)

class MenuTeste(Menu):
	def __init__(self, gestorEscolar):
		Menu.__init__(self, gestorEscolar)
		self.botoes = BotaoLayout(1, 1)
		self.botoes.addBotao("entrar", self.entrar)
		self.botoes.addBotao("registrar", self.entrar)
		self.botoes.addBotao("logar", self.entrar)
		self.botoes.addBotao("sair", self.gestorEscolar.sair)
		
		self.widgets.append(self.botoes)
#		self.opcoes = ["entrar", "sair"]
#		self.funcoes = [self.entrar, self.gestorEscolar.sair]
	
	def entrar(self):
		self.gestorEscolar.novoMenu(MenuTeste2)
		
	def show(self, tela):
		self.showWidgets(tela)
		#self.showOpcoes(tela)
		
class MenuTeste2(Menu):
	def __init__(self, gestorEscolar):
		Menu.__init__(self, gestorEscolar)
		self.opcoes = ["voltar"]
		self.funcoes = [self.voltar]
	
	def voltar(self):
		self.gestorEscolar.novoMenu(MenuTeste)
		
	def show(self, tela):
		self.showOpcoes(tela)
		