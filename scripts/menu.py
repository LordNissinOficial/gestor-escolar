import curses
from scripts.widgets.botao import Botao#botaoLayout import BotaoLayout
from scripts.widgets.textoInput import TextoInput

class Menu:
	def __init__(self, gestorEscolar):
		self.gestorEscolar = gestorEscolar
		self.widgets = []
		self.widgetAtual = 0
	
	def lidarInput(self, key):
		
		if key==curses.KEY_DOWN:
			self.widgetAtual = min(len(self.widgets)-1, self.widgetAtual+1)
		elif key==curses.KEY_UP:
			self.widgetAtual = max(0, self.widgetAtual-1)
		else:
			self.widgets[self.widgetAtual].lidarInput(key)
	
	def showWidgets(self, tela):
		for index, widget in enumerate(self.widgets):
			widget.show(tela, index==self.widgetAtual)
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
		self.botoes.horizontal = True
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
		self.showWidgets(tela)

class MenuInicial(Menu):
	def __init__(self, gestorEscolar):
		Menu.__init__(self, gestorEscolar)
		#self.botoes = []
		self.widgets = [Botao(1, 1, "registrar", lambda: gestorEscolar.novoMenu(MenuRegistrar)), Botao(1, 2, "logar", lambda: gestorEscolar.novoMenu(MenuLogar)), Botao(1, 3, "sair", gestorEscolar.sair)]

		
	def show(self, tela):
		self.showWidgets(tela)
		#self.botoes.addBotao("registrar", self.registrar)
#		self.botoes.addBotao("logar", self.logar)
#		self.botoes.addBotao("sair", self.gestorEscolar.sair)
	
class MenuRegistrar(Menu):
	def __init__(self, gestorEscolar):
		Menu.__init__(self, gestorEscolar)
		self.widgets = [Botao(1, 1, "nome:", None), Botao(1, 2, "senha:", None), TextoInput(1, 3, "nome")]
		
	def show(self, tela):
		self.showWidgets(tela)	
		
class MenuLogar(Menu):
	def __init__(self, gestorEscolar):
		Menu.__init__(self, gestorEscolar)
		self.widgets = [Botao(1, 1, "nome logar:", None), Botao(1, 2, "senha:", None)]
		
	def show(self, tela):
		self.showWidgets(tela)	