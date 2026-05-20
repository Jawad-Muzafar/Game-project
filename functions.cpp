#include "main.h"
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

char grid[3][3] = {{'1','2','3'},{'4','5','6'},{'7','8','9'}};
char playerMarker = 'X';
char computerMarker = 'O';

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
    // Simple random move
    int slot;
    while (true) {
        slot = (rand() % 9) + 1;
        if (placeMarker(slot, computerMarker))
            break;
    }
}

void playGame() {
    // Reset board
    char startGrid[3][3] = {{'1','2','3'},{'4','5','6'},{'7','8','9'}};
    for (int r = 0; r < 3; ++r)
        for (int c = 0; c < 3; ++c)
            grid[r][c] = startGrid[r][c];

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

    int currentPlayer = 1; // 1 = human, 2 = computer
    drawBoard();
    while (true) {
        if (currentPlayer == 1) {
            playerMove();
        } else {
            computerMove();
        }
        drawBoard();
        char result = checkWin();
        if (result == playerMarker) {
            cout << "You win!\n";
            break;
        } else if (result == computerMarker) {
            cout << "Computer wins!\n";
            break;
        } else if (result == 'D') {
            cout << "It's a draw!\n";
            break;
        }
        currentPlayer = (currentPlayer == 1) ? 2 : 1;
    }
}
