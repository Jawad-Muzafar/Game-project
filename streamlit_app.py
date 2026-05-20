import streamlit as st
import random

st.set_page_config(page_title="Tic-Tac-Toe", layout="centered")

# Helpers
st.title ("Tic-Tac-Toe Game -  made by  Muhammad Jawad Muzafar khan")
def init_state():
    if 'grid' not in st.session_state:
        st.session_state.grid = [str(i) for i in range(1,10)]
    if 'player_marker' not in st.session_state:
        st.session_state.player_marker = 'X'
    if 'computer_marker' not in st.session_state:
        st.session_state.computer_marker = 'O'
    if 'turn' not in st.session_state:
        st.session_state.turn = 'player'
    if 'message' not in st.session_state:
        st.session_state.message = ''
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False


def check_win(grid):
    # rows and cols
    for i in range(3):
        if grid[3*i] == grid[3*i+1] == grid[3*i+2]:
            return grid[3*i]
        if grid[i] == grid[i+3] == grid[i+6]:
            return grid[i]
    # diagonals
    if grid[0] == grid[4] == grid[8]:
        return grid[0]
    if grid[2] == grid[4] == grid[6]:
        return grid[2]
    # draw
    if all(cell in ('X','O') for cell in grid):
        return 'D'
    return None


def computer_move():
    # Minimax-based optimal move
    grid = st.session_state.grid
    player = st.session_state.player_marker
    computer = st.session_state.computer_marker

    def available_moves(g):
        return [i for i, c in enumerate(g) if c not in ('X', 'O')]

    def apply_move(g, idx, mark):
        ng = g.copy()
        ng[idx] = mark
        return ng

    def score_for(winner, depth):
        if winner == computer:
            return 10 - depth
        if winner == player:
            return depth - 10
        return 0

    def minimax(g, depth, is_maximizing):
        winner = check_win(g)
        if winner is not None:
            if winner == 'D':
                return 0
            return score_for(winner, depth)

        moves = available_moves(g)
        if is_maximizing:
            best_score = -999
            for m in moves:
                ng = apply_move(g, m, computer)
                sc = minimax(ng, depth + 1, False)
                if sc > best_score:
                    best_score = sc
            return best_score
        else:
            best_score = 999
            for m in moves:
                ng = apply_move(g, m, player)
                sc = minimax(ng, depth + 1, True)
                if sc < best_score:
                    best_score = sc
            return best_score

    moves = available_moves(grid)
    if not moves:
        return

    best_move = None
    best_score = -999
    for m in moves:
        ng = apply_move(grid, m, computer)
        sc = minimax(ng, 0, False)
        if sc > best_score:
            best_score = sc
            best_move = m

    # place the best move
    if best_move is not None:
        st.session_state.grid[best_move] = computer


# Initialize
init_state()

st.title("Tic-Tac-Toe")

# Add CSS to style the board cells with visible grid lines
st.markdown("""
<style>
div.stButton > button {height:80px; width:80px; font-size:32px; border:2px solid #444; background-color:#fff;}
div[data-testid="stMarkdownContainer"] div.cell {height:80px; width:80px; display:flex; align-items:center; justify-content:center; border:2px solid #444; font-size:36px}
div.row-widget.stButton {padding:0}
</style>
""", unsafe_allow_html=True)

# Controls: choose marker and restart
choice = st.radio("Choose your marker:", ['X','O'], index=0)
starter = st.radio("Who starts?", ['Player', 'Computer'], index=0)
if st.button("Start / Restart"):
    st.session_state.player_marker = choice
    st.session_state.computer_marker = 'O' if choice == 'X' else 'X'
    st.session_state.grid = [str(i) for i in range(1,10)]
    st.session_state.turn = 'player' if starter == 'Player' else 'computer'
    st.session_state.game_over = False
    st.session_state.message = ''
    # If computer starts, make its first optimal move immediately
    if st.session_state.turn == 'computer':
        computer_move()
        res = check_win(st.session_state.grid)
        if res == st.session_state.computer_marker:
            st.session_state.message = 'Computer wins!'
            st.session_state.game_over = True
        elif res == 'D':
            st.session_state.message = "It's a draw!"
            st.session_state.game_over = True
        else:
            st.session_state.turn = 'player'

# Display board
cols = st.columns(3)
for r in range(3):
    row_cols = st.columns(3)
    for c in range(3):
        idx = r*3 + c
        with row_cols[c]:
            cell = st.session_state.grid[idx]
            if cell in ('X','O'):
                st.markdown(f"<div class='cell'>{cell}</div>", unsafe_allow_html=True)
            else:
                if not st.session_state.game_over and st.session_state.turn == 'player':
                    if st.button(cell, key=f"cell_{idx}"):
                        # player move
                        st.session_state.grid[idx] = st.session_state.player_marker
                        res = check_win(st.session_state.grid)
                        if res == st.session_state.player_marker:
                            st.session_state.message = 'You win!'
                            st.session_state.game_over = True
                        elif res == 'D':
                            st.session_state.message = "It's a draw!"
                            st.session_state.game_over = True
                        else:
                            st.session_state.turn = 'computer'
                else:
                    # non-interactive empty cell styled to match the grid
                    st.markdown(f"<div class='cell' style='color:#666'>{cell}</div>", unsafe_allow_html=True)

# If it's computer's turn and game not over, make a move
if st.session_state.turn == 'computer' and not st.session_state.game_over:
    computer_move()
    res = check_win(st.session_state.grid)
    if res == st.session_state.computer_marker:
        st.session_state.message = 'Computer wins!'
        st.session_state.game_over = True
    elif res == 'D':
        st.session_state.message = "It's a draw!"
        st.session_state.game_over = True
    else:
        st.session_state.turn = 'player'

# Message / status
st.write('')
if st.session_state.message:
    st.success(st.session_state.message)
else:
    if st.session_state.game_over:
        st.info('Game over. Click Start / Restart to play again.')
    else:
        st.info(f"Turn: {st.session_state.turn}")
