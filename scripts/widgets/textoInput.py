import curses

class TextoInput:
	def __init__(self, x, y, label, largura=32):
		self.x = x
		self.y = y
		self.label = label
		self.largura = largura
		self.texto = ""
		
	def lidarInput(self, key):
		if ((key>=ord("a") and key<=ord("z")) or (key>=ord("A") and key<=ord("Z"))) and len(self.texto)<self.largura:
			self.texto += chr(key)
		elif key==ord(" ") and self.texto[-1]!=" " and len(self.texto)<self.largura-1:
			self.texto += " "
		elif key==curses.KEY_DC or key==126:
			self.texto = self.texto[:len(self.texto)-1]
			
	def show(self, tela, highlight):
		if highlight:
			tela.addstr(self.y, self.x, self.label+":")
			tela.addstr(self.y, self.x+len(self.label)+1, self.texto+" "*(self.largura-len(self.texto)), curses.A_REVERSE)
		else:
			tela.addstr(self.y, self.x, self.label+":")
			tela.addstr(self.y, self.x+len(self.label)+1, self.texto)
	