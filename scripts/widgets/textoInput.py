import curses

class TextoInput:
	def __init__(self, x, y, largura=50, esconder=False, charsProibidos=""):
		self.x = x
		self.y = y
#		self.label = label
		self.largura = largura
		self.esconder = esconder
		self.texto = ""
		self.charsProibidos = [ord(char) for char in charsProibidos]
		
	def lidarInput(self, key):
		if key in self.charsProibidos: return 
		if ((key>=ord("a") and key<=ord("z")) or (key>=ord("A") and key<=ord("Z"))) and len(self.texto)<self.largura:
			self.texto += chr(key)
		elif len(self.texto) and key==ord(" ") and self.texto[-1]!=" " and len(self.texto)<self.largura-1:
			self.texto += " "
		elif key==curses.KEY_DC or key==126:
			self.texto = self.texto[:len(self.texto)-1]
			
	def show(self, tela, highlight):
		atributo = curses.A_REVERSE if highlight else 0
		texto = "*"*len(self.texto) if self.esconder else self.texto		
		tela.addstr(self.y, self.x, texto+" "*(self.largura-len(texto)), atributo)	