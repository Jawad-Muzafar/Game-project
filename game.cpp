#include "main.h"
#include "functions.cpp"
#include <iostream>
#include <ctime>

using namespace std;

int main(){
	srand((unsigned)time(nullptr));
	playGame();
	return 0;
}