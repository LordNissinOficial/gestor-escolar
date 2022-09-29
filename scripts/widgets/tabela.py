import curses

class Tabela:
	def __init__(self, x, y, tabelas):
		self.x = x
		self.y = y
		self.tabelas = tabelas
		
	def show(self, tela):
		tabelaOffset = 0
		for tabela in self.tabelas:
			
			offset = len(tabela)
			for index, conteudo in enumerate(self.tabelas[tabela]):
				tela.addstr(self.y+index+1, self.x+tabelaOffset, str(conteudo))
				offset = max(offset, len(str(conteudo)))
			tela.addstr(self.y, self.x+tabelaOffset, tabela)
			tabelaOffset += offset+1