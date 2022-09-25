#include <ncurses.h>
#include <string>
#include "scripts/gestorEscolar.h"
int main(int argc, char *argv[])
{
	int menuAtual = 1;
	//const char * image[8] = {
//		"□□■■■■□□",
//		"□■□□□□■□",
//		"□■□□□□■□",
//		"□■□□□□■□",
//		"□■□□□□■□",
//		"□■□□□□■□",
//		"□■□□□□■□",
//		"□□■■■■□□"
//	};
	initscr();
	noecho();
	curs_set(0);
	//getch();
	//GestorEscolar gestorEscolar = GestorEscolar();
	//gestorEscolar.menuAtual = 2;
	while (1) {
		if (update(menuAtual)) {
			break;
		}
		show(menuAtual);
	}
	//getch();
	endwin();

}