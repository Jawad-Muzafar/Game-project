# Tic-Tac-Toe Game 🎮

A C++ implementation of the classic Tic-Tac-Toe game with an intelligent computer opponent featuring three difficulty levels.

---

## 📋 Project Overview

This is an interactive command-line Tic-Tac-Toe game where you play against a computer AI. The game tracks scores across multiple rounds and offers three difficulty levels to challenge players of all skill levels.

---

## ✨ Features

### Game Modes
- **Player vs Computer**: Challenge the AI opponent
- **Marker Selection**: Choose to play as 'X' or 'O'
- **Difficulty Levels**:
  - **Level 1 (Easy)**: Computer makes mostly random moves with 50% chance of mistakes
  - **Level 2 (Medium)**: Computer plays strategically with 15% chance of mistakes
  - **Level 3 (Hard)**: Computer plays optimally with only 4% chance of mistakes

### Smart AI Features
- **Win Detection**: Computer identifies and takes winning moves
- **Defense**: Computer blocks your winning moves
- **Strategic Play**: Prioritizes center and corner positions in hard mode
- **Human-like Mistakes**: Lower difficulty levels intentionally make suboptimal moves for balance

### Game Features
- **Score Tracking**: Keeps running score across multiple games
- **Random Starter**: Either player or computer can start each round
- **Input Validation**: Robust error handling for invalid moves
- **Board Display**: Clear, formatted grid display after each move
- **Replay Option**: Play multiple rounds without restarting

---

## 🛠️ Technical Details

### File Structure
```
Game-project/
├── main.h                 # Header file with function declarations
├── functions.cpp          # Core game logic and AI implementation
├── game.cpp              # Main entry point
└── README.md             # This file
```

### Key Components

#### 1. **main.h** - Header File
Declares all game functions:
- `drawBoard()`: Displays the current game board
- `placeMarker()`: Places a player's marker on the board
- `checkWin()`: Checks for win, loss, or draw conditions
- `playerMove()`: Handles player input and move validation
- `computerMove()`: Implements AI logic with difficulty levels
- `playGame()`: Main game loop
- `chooseDifficulty()`: Difficulty selection menu
- `resetBoard()`: Resets board for new round
- `showScores()`: Displays current score

#### 2. **functions.cpp** - Game Logic
**Global Variables:**
- `grid[3][3]`: 3x3 game board
- `playerMarker`: Player's symbol ('X' or 'O')
- `computerMarker`: Computer's symbol
- `playerScore`, `computerScore`, `drawScore`: Tracking wins and draws
- `difficulty`: Current difficulty level (1-3)

**Key Functions:**

**drawBoard()**
- Clears screen and displays formatted board
- Shows board with grid lines

**placeMarker(slot, marker)**
- Validates if a cell is empty
- Places the marker if valid
- Returns success/failure

**checkWin()**
- Checks rows, columns, and diagonals for three in a row
- Returns: player marker (win), computer marker (loss), 'D' (draw), 'N' (no result)

**playerMove()**
- Prompts for number 1-9
- Validates input range and cell availability
- Loops until valid move is made

**computerMove()**
- Implements difficulty-based strategy:
  - All levels: Try to win if beneficial
  - Level 2+: Block player's winning moves
  - Level 3: Prioritize center (5) and corners (1,3,7,9)
  - Fallback: Random available cell
- Uses `findWinningMove()` helper for strategic moves
- Mistake probability: Easy 50%, Medium 15%, Hard 4%

**chooseDifficulty()**
- Menu selection for difficulty (1-3)
- Input validation for valid range

**playGame()**
- Main game loop
- Marker selection
- Multiple round support
- Score tracking and display
- Replay prompt

#### 3. **game.cpp** - Entry Point
- Seeds random number generator
- Calls `playGame()` to start the game

---

## 🎯 How to Play

### Starting the Game
1. Compile and run the program
2. Choose your marker: **X** or **O**
3. Select difficulty level:
   - **1** for Easy
   - **2** for Medium
   - **3** for Hard

### During the Game
- Board positions are numbered 1-9:
  ```
   1 | 2 | 3
  ---|---|---
   4 | 5 | 6
  ---|---|---
   7 | 8 | 9
  ```
- Enter a number (1-9) to place your marker
- Get three in a row (horizontal, vertical, or diagonal) to win
- Computer makes its move automatically
- Game ends when someone wins or board is full

### After Each Game
- Scores are displayed
- Choose to play again or exit
- Optionally change difficulty for next round

---

## 🎮 Game Rules

1. **Valid Moves**: Only place markers in empty cells
2. **Winning**: First to get 3 in a row wins
3. **Draw**: If board is full with no winner, it's a draw
4. **Turn Order**: Random selection determines who starts each round
5. **Score Tracking**: Wins and draws are tracked throughout session

---

## 📊 Difficulty Comparison

| Feature | Easy | Medium | Hard |
|---------|------|--------|------|
| Mistake Probability | 50% | 15% | 4% |
| Strategic Moves | Random | Win + Block | Win + Block + Positioning |
| Center/Corner Preference | No | No | Yes |
| Challenge Level | Beginner | Intermediate | Expert |

---

## 🔧 Compilation Instructions

### Prerequisites
- C++ compiler (g++, clang, or MSVC)
- Standard C++ library

### Compile
```bash
g++ -o TicTacToe game.cpp -std=c++11
```

### Run
```bash
./TicTacToe
```

---

## 📝 Example Game Session

```
Choose your marker (X or O): X
Choose difficulty: 1) Easy  2) Medium  3) Hard : 2

 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9

Enter the number (1-9) where you want to place your marker: 5

 1 | 2 | 3
---|---|---
 4 | X | 6
---|---|---
 7 | 8 | 9

 1 | 2 | 3
---|---|---
 4 | X | O
---|---|---
 7 | 8 | 9

[Game continues...]

You win!
Score - You: 1  Computer: 0  Draws: 0
Play again? (Y/N) Y
```

---

## 🎓 Learning Objectives

This project demonstrates:
- **Data Structures**: 2D arrays for game board
- **Algorithm Design**: Game state checking and AI logic
- **Control Flow**: Game loops and decision trees
- **Input Validation**: User input handling and error management
- **Modular Programming**: Separate functions for different game aspects
- **AI Implementation**: Basic artificial intelligence with difficulty scaling
- **Probability**: Random decision-making with weighted outcomes

---

## 💡 Code Highlights

### AI Strategy (computerMove function)
The AI uses a sophisticated approach:
1. Calculate mistake probability based on difficulty
2. If confident enough, look for winning moves
3. If no winning move, block player's winning opportunities
4. On hard mode, prioritize strategic positions (center/corners)
5. Fall back to random available cell if no strategic move exists

### Win Checking (checkWin function)
Efficiently checks all possible winning combinations:
- 3 rows
- 3 columns
- 2 diagonals
- Draw condition (no empty cells)

### Input Validation
Robust error handling for:
- Non-numeric input
- Out-of-range numbers (1-9)
- Already occupied cells
- Invalid marker selection

---

## 🚀 Future Enhancements

Potential improvements:
- Graphical user interface (GUI)
- Minimax algorithm for perfect AI
- Larger board sizes (4x4, 5x5)
- Online multiplayer support
- Game statistics and history
- Sound effects and animations
- Undo/Redo functionality

---

## 📜 License

This project is created for educational purposes.

---

## 👨‍💻 Author

**Jawad Muzafar**

---

## 🤝 Contributing

Feel free to fork, improve, and submit pull requests with enhancements!

---

## 📞 Support

For issues or questions, please create an issue in the repository.

---

**Enjoy playing Tic-Tac-Toe! Challenge the AI and see if you can beat it! 🏆**
