import curses
from scripts.gestorEscolar import GestorEscolar

def main(tela):
	#tela = curses.initscr()
	gestorEscolar = GestorEscolar(tela)
	tela.keypad(True)
	curses.noecho()
	curses.cbreak()
	curses.curs_set(0)
	
	while gestorEscolar.rodando:
		gestorEscolar.show()		
		gestorEscolar.lidarInput()
	
	tela.keypad(False)
	curses.cbreak()
	curses.echo()
	curses.endwin()

curses.wrapper(main)