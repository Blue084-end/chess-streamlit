import streamlit as st
from chess.game import Game
from PIL import Image

st.set_page_config(page_title="Cờ Tướng Online", layout="wide")
st.title("♟️ Cờ Tướng Streamlit")

# Khởi tạo game
if "game" not in st.session_state:
    st.session_state.game = Game()

game = st.session_state.game
st.subheader(f"Lượt chơi: {game.turn.capitalize()}")

# Hiển thị bàn cờ nền
board_img = Image.open("assets/ban_co.png")
st.image(board_img, caption="Bàn cờ tướng", use_column_width=True)

# Hiển thị quân cờ
st.write("### Vị trí quân cờ hiện tại:")
for row_idx, row in enumerate(game.board.grid):
    cols = st.columns(9)
    for col_idx, piece in enumerate(row):
        if piece:
            image_path = f"assets/{piece.color}_pieces/{piece.name}.png"
            try:
                cols[col_idx].image(image_path, width=60)
            except:
                cols[col_idx].text(piece.name)
        else:
            cols[col_idx].empty()

# Tương tác đơn giản
from_row = st.number_input("Từ hàng", min_value=0, max_value=9, step=1)
from_col = st.number_input("Từ cột", min_value=0, max_value=8, step=1)
to_row = st.number_input("Đến hàng", min_value=0, max_value=9, step=1)
to_col = st.number_input("Đến cột", min_value=0, max_value=8, step=1)

if st.button("Thực hiện nước đi"):
    game.make_move((from_row, from_col), (to_row, to_col))
    st.success("Đã thực hiện nước đi!")
