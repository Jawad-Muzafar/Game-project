#ifndef MAIN_H
#define MAIN_H

void drawBoard();
bool placeMarker(int slot, char marker);
char checkWin();
void playerMove();
void computerMove();
void playGame();
int chooseDifficulty();
void resetBoard();
void showScores();

#endif // MAIN_H