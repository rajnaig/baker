import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def calculate_divisions(length, width, min_piece_size):
    divisions_length = max(1, int(length // min_piece_size))
    divisions_width = max(1, int(width // min_piece_size))
    return divisions_length, divisions_width

def plot_divisions(length, width, divisions_length, divisions_width):
    fig, ax = plt.subplots()
    rectangle = patches.Rectangle((0, 0), length, width, edgecolor='#059b76', facecolor="none")
    ax.add_patch(rectangle)
    for i in range(1, divisions_length):
        ax.plot([i * length / divisions_length, i * length / divisions_length], [0, width], color='#c22b6c')
    for j in range(1, divisions_width):
        ax.plot([0, length], [j * width / divisions_width, j * width / divisions_width], color='#c22b6c')
    ax.set_xlim(0, length)
    ax.set_ylim(0, width)
    return fig

# Streamlit felhasználói felület
st.title("Baker's Design Calculator")

# Beviteli mezők
length = st.number_input("Length (cm):", min_value=0.1, value=1.0, step=0.1)
width = st.number_input("Width (cm):", min_value=0.1, value=1.0, step=0.1)
min_piece_size = st.number_input("Minimum Piece Size (cm):", min_value=0.1, value=1.0, step=0.1)

if st.button("Calculate Divisions"):
    divisions_length, divisions_width = calculate_divisions(length, width, min_piece_size)
    piece_width = width / divisions_width
    piece_length = length / divisions_length
    st.write(f"Piece size: {piece_length:.2f} cm x {piece_width:.2f} cm")
    fig = plot_divisions(length, width, divisions_length, divisions_width)
    st.pyplot(fig)
