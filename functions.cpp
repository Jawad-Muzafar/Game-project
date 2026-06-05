#include "main.h"
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>

using namespace std;

char grid[3][3] = {{'1','2','3'},{'4','5','6'},{'7','8','9'}};
char playerMarker = 'X';
char computerMarker = 'O';
int playerScore = 0;
int computerScore = 0;
int drawScore = 0;
int difficulty = 2; 

void drawBoard() {
    system("cls");
    cout << " " << grid[0][0] << " | " << grid[0][1] << " | " << grid[0][2] << " " << endl;
    cout << "---|---|---" << endl;
    cout << " " << grid[1][0] << " | " << grid[1][1] << " | " << grid[1][2] << " " << endl;
    cout << "---|---|---" << endl;
    cout << " " << grid[2][0] << " | " << grid[2][1] << " | " << grid[2][2] << " " << endl;
}

bool placeMarker(int slot, char marker) {
    int row = (slot - 1) / 3;
    int col = (slot - 1) % 3;
    if (grid[row][col] != 'X' && grid[row][col] != 'O') {
        grid[row][col] = marker;
        return true;
    }
    return false;
}

char checkWin() {
    // Rows and columns
    for (int i = 0; i < 3; ++i) {
        if (grid[i][0] == grid[i][1] && grid[i][1] == grid[i][2])
            return grid[i][0];
        if (grid[0][i] == grid[1][i] && grid[1][i] == grid[2][i])
            return grid[0][i];
    }
    // Diagonals
    if (grid[0][0] == grid[1][1] && grid[1][1] == grid[2][2])
        return grid[0][0];
    if (grid[0][2] == grid[1][1] && grid[1][1] == grid[2][0])
        return grid[0][2];

    // Check for draw (no digits left)
    bool emptyFound = false;
    for (int r = 0; r < 3; ++r)
        for (int c = 0; c < 3; ++c)
            if (grid[r][c] != 'X' && grid[r][c] != 'O')
                emptyFound = true;
    if (!emptyFound)
        return 'D'; // Draw

    return 'N'; // No winner yet
}

void playerMove() {
    int slot;
    while (true) {
        cout << "Enter the number (1-9) where you want to place your marker: ";
        if (!(cin >> slot)) {
            cin.clear();
            cin.ignore(10000, '\n');
            cout << "Invalid input.\n";
            continue;
        }
        if (slot < 1 || slot > 9) {
            cout << "Invalid move. Please enter a number between 1 and 9.\n";
            continue;
        }
        if (placeMarker(slot, playerMarker))
            break;
        cout << "Cell already occupied. Choose another cell.\n";
    }
}

void computerMove() {
    // Computer move varies by difficulty.
    auto isFree = [](int s)->bool{
        int row = (s - 1) / 3;
        int col = (s - 1) % 3;
        return (grid[row][col] != 'X' && grid[row][col] != 'O');
    };

    auto findWinningMove = [&](char mark)->int{
        for (int s = 1; s <= 9; ++s) {
            if (!isFree(s)) continue;
            int r = (s - 1) / 3;
            int c = (s - 1) % 3;
            char old = grid[r][c];
            grid[r][c] = mark;
            char res = checkWin();
            grid[r][c] = old;
            if (res == mark) return s;
        }
        return -1;
    };

    int slot = -1;
    // Small chance to make a mistake to make the game feel more human
    double mistakeProb = (difficulty == 1) ? 0.5 : (difficulty == 2 ? 0.15 : 0.04);

    if (difficulty >= 2) {
        // Try to win
        if (((double)rand() / RAND_MAX) > mistakeProb) {
            slot = findWinningMove(computerMarker);
        }
        // Try to block
        if (slot == -1 && ((double)rand() / RAND_MAX) > mistakeProb) {
            slot = findWinningMove(playerMarker);
        }
    }

    if (difficulty == 3 && slot == -1) {
        // Try take center
        if (isFree(5)) slot = 5;
        // Try corners
        int corners[4] = {1,3,7,9};
        if (slot == -1) {
            for (int i = 0; i < 4; ++i) if (isFree(corners[i])) { slot = corners[i]; break; }
        }
    }

    // Fallback to random available slot
    if (slot == -1) {
        while (true) {
            int s = (rand() % 9) + 1;
            if (isFree(s)) { slot = s; break; }
        }
    }

    placeMarker(slot, computerMarker);
}

void resetBoard() {
    char startGrid[3][3] = {{'1','2','3'},{'4','5','6'},{'7','8','9'}};
    for (int r = 0; r < 3; ++r)
        for (int c = 0; c < 3; ++c)
            grid[r][c] = startGrid[r][c];
}

int chooseDifficulty() {
    cout << "Choose difficulty: 1) Easy  2) Medium  3) Hard : ";
    int d;
    while (true) {
        if (!(cin >> d)) { cin.clear(); cin.ignore(10000,'\n'); cout << "Invalid input. Choose 1,2 or 3: "; continue; }
        if (d >=1 && d <=3) break;
        cout << "Choose 1, 2 or 3: ";
    }
    difficulty = d;
    return d;
}

void showScores() {
    cout << "Score - You: " << playerScore << "  Computer: " << computerScore << "  Draws: " << drawScore << "\n";
}

void playGame() {
    // Main game loop with scoring, replay, difficulty and random starter
    playerScore = computerScore = drawScore = 0;

    cout << "Choose your marker (X or O): ";
    char choice;
    cin >> choice;
    while (choice != 'X' && choice != 'O' && choice != 'x' && choice != 'o') {
        cout << "Invalid choice. Please select X or O: ";
        cin >> choice;
    }
    if (choice == 'X' || choice == 'x') {
        playerMarker = 'X';
        computerMarker = 'O';
    } else {
        playerMarker = 'O';
        computerMarker = 'X';
    }

    chooseDifficulty();

    bool playAgain = true;
    while (playAgain) {
        resetBoard();
        // Randomly pick who starts
        int currentPlayer = (rand() % 2) ? 1 : 2; // 1 human, 2 computer
        drawBoard();

        while (true) {
            if (currentPlayer == 1) playerMove(); else computerMove();
            drawBoard();
            char result = checkWin();
            if (result == playerMarker) {
                cout << "You win!\n";
                playerScore++;
                break;
            } else if (result == computerMarker) {
                cout << "Computer wins!\n";
                computerScore++;
                break;
            } else if (result == 'D') {
                cout << "It's a draw!\n";
                drawScore++;
                break;
            }
            currentPlayer = (currentPlayer == 1) ? 2 : 1;
        }

        showScores();
        cout << "Play again? (Y/N) ";
        char again;
        cin >> again;
        if (again == 'Y' || again == 'y') {
            cout << "Keep same difficulty? (Y to keep, N to change): ";
            char ch; cin >> ch;
            if (ch == 'N' || ch == 'n') chooseDifficulty();
            // keep same markers
            continue;
        } else {
            playAgain = false;
        }
    }
}
