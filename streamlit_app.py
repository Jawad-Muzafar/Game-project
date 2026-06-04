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
    # Light strategy + randomness so outcomes are not always draws
    grid = st.session_state.grid
    player = st.session_state.player_marker
    computer = st.session_state.computer_marker

    def available_moves(g):
        return [i for i, c in enumerate(g) if c not in ('X', 'O')]

    def find_winning_move(mark):
        for m in available_moves(grid):
            ng = grid.copy()
            ng[m] = mark
            if check_win(ng) == mark:
                return m
        return None

    moves = available_moves(grid)
    if not moves:
        return

    # 1) Win if possible
    winning = find_winning_move(computer)
    if winning is not None:
        st.session_state.grid[winning] = computer
        return

    # 2) Block player's immediate win
    block = find_winning_move(player)
    if block is not None:
        st.session_state.grid[block] = computer
        return

    # 3) Otherwise pick randomly (slight center/corner preference)
    # Index map is 0..8 left-to-right, top-to-bottom: 4=center; 0/2/6/8=corners.
    preferred = [4, 0, 2, 6, 8]
    preferred_moves = [m for m in preferred if m in moves]
    candidates = preferred_moves if preferred_moves else moves
    st.session_state.grid[random.choice(candidates)] = computer


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
