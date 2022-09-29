from scripts.menu import Menu
from scripts.widgets.tabela import Tabela

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
			#print(len())
			for index, nota in enumerate(notas[materia]):
				tabelas[f"prova {index+1}"].append(nota)
			tabelas["media"].append(self.calcularMedia(materia))
		
	def calcularMedia(self, notas):
		return round(float(sum(notas)), 2)