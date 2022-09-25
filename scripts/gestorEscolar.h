#include <ncurses.h>

int update(int &menuAtual) {
	int key = getch();
	if (key==(int)'o') {
		menuAtual = 2;
	}	else if (key==(int)'q') {
			return 1;
		}	else {
				menuAtual = 1;
			}
	
	return  0;
};
void show(int menuAtual) {
//	return 1;
	//menuAtual = 1;
	clear();
	if (menuAtual==1) {
		mvprintw(4, 5, "[q] para sair");
	}	else if (menuAtual==2) {
		mvprintw(4, 5, "[q] para sair 2");
	}
	refresh();
};