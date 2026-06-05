#include "main.h"
#include "functions.cpp"
#include <iostream>
#include <ctime>

using namespace std;

int main(){
	srand((unsigned)time(NULL));
	playGame();
	return 0;
}