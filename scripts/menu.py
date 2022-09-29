import curses
#from scripts.estudante.menuNotas import MenuNotas
from scripts.widgets.botao import Botao#botaoLayout import BotaoLayout
from scripts.widgets.textoInput import TextoInput
from scripts.widgets.label import Label
from scripts.widgets.tabela import Tabela

class Menu:
	def __init__(self, gestorEscolar):
		self.gestorEscolar = gestorEscolar
		self.widgets = []
		self.labels = []
		self.widgetAtual = 0
	
	def lidarInput(self, key):		
		if key==curses.KEY_DOWN:
			self.widgetAtual = min(len(self.widgets)-1, self.widgetAtual+1)
		elif key==curses.KEY_UP:
			self.widgetAtual = max(0, self.widgetAtual-1)
		else:
			if len(self.widgets):
				self.widgets[self.widgetAtual].lidarInput(key)
	
	def showWidgets(self, tela):
		for index, widget in enumerate(self.widgets):
			widget.show(tela, index==self.widgetAtual)
		
		for label in self.labels:
			label.show(tela)
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
		self.widgets = [Botao(1, 1, "registrar", None), Botao(1, 2, "logar", lambda: gestorEscolar.novoMenu(MenuLogar)), Botao(1, 3, "sair", gestorEscolar.sair)]

		
	def show(self, tela):
		self.showWidgets(tela)
		#self.botoes.addBotao("registrar", self.registrar)
#		self.botoes.addBotao("logar", self.logar)
#		self.botoes.addBotao("sair", self.gestorEscolar.sair)
	
class MenuRegistrar(Menu):
	def __init__(self, gestorEscolar):
		Menu.__init__(self, gestorEscolar)
		self.widgets = [Botao(1, 1, "nome:", None), Botao(1, 2, "senha:", None)]
		
	def show(self, tela):
		self.showWidgets(tela)	
		
class MenuLogar(Menu):
	def __init__(self, gestorEscolar):
		Menu.__init__(self, gestorEscolar)
		self.widgets = [TextoInput(8, 2), TextoInput(8, 3, 16, True), Botao(1, 4, "logar", lambda: gestorEscolar.logarUsuario(self.widgets[0].texto, self.widgets[1].texto))]
		self.labels = [Label(1, 2, "nome:"), Label(1, 3, "senha:")]
		
	def show(self, tela):
		self.showWidgets(tela)
		
class MenuPrincipal(Menu):
	def __init__(self, gestorEscolar):
		Menu.__init__(self, gestorEscolar)
		self.widgets = [Botao(1, 1, "estudante", lambda: gestorEscolar.novoMenu(MenuEstudante)), Botao(1, 2, "professor"), Botao(1, 3, "bibliotecario")]
	
	def show(self, tela):
		self.showWidgets(tela)
		
	
class MenuEstudante(Menu):
	def __init__(self, gestorEscolar):
		Menu.__init__(self, gestorEscolar)
		self.widgets = [Botao(1, 1, "notas", lambda: gestorEscolar.novoMenu(MenuNotas)), Botao(1, 2, "aulas do dia")]
	
	def show(self, tela):
		self.showWidgets(tela)

class MenuNotas(Menu):
	def __init__(self, gestorEscolar):
		Menu.__init__(self, gestorEscolar)
		notas = {"ciencias": [7, 7, 7, 7, 7], "matematica": [7, 7, 7, 7, 7], "artes": [7, 7, 7, 7, 7], "portugues": [7, 7, 7, 7, 7]}
		self.labels = [Tabela(4, 1, self.conseguirTabelas(notas))]
	
	def conseguirTabelas(self, notas):
		tabelas = {}
		tabelas["materias"] = notas.keys()
		tabelas["prova 1"] = []
		tabelas["prova 2"] = []
		tabelas["prova 3"] = []
		tabelas["prova 4"] = []
		tabelas["prova 5"] = []
		tabelas["prova 6"] = []
		tabelas["media"] = []
		
		for materia in notas:
			for index, nota in enumerate(notas[materia]):
				tabelas[f"prova {index+1}"].append(nota)
			tabelas["media"].append(self.calcularMedia(notas[materia]))
		return tabelas
		
	def calcularMedia(self, notas):
		return round(float(sum(notas)/len(notas)), 2)
		
	def show(self, tela):
		self.showWidgets(tela)