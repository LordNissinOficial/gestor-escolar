from scripts.privilegios import privilegios

class Usuario:
	def __init__(self, nome, senha, rank, data, privilegiosEditados=None):
		self.nome = nome
		self.senha = senha
		self.data = data
		self.rank = rank
		if privilegiosEditados:
			self.privilegios = privilegiosEditados
		else:
			self.privilegios = privilegios[rank]