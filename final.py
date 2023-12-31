import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def calculate_divisions(length, width, min_piece_size):
    divisions_length = max(1, length // min_piece_size)
    divisions_width = max(1, width // min_piece_size)
    return int(divisions_length), int(divisions_width)

def plot_divisions(length, width, divisions_length, divisions_width):
    fig, ax = plt.subplots()
    ax.set_facecolor('#343541')
    rectangle = patches.Rectangle((0, 0), length, width, edgecolor='#059b76', facecolor="none")
    ax.add_patch(rectangle)
    for i in range(1, divisions_length):
        ax.axvline(x=i * length / divisions_length, color='#c22b6c')
    for j in range(1, divisions_width):
        ax.axhline(y=j * width / divisions_width, color='#c22b6c')
    ax.set_xlim(0, length)
    ax.set_ylim(0, width)
    return fig

st.title("Baker's Design Calculator")

# Csúszkák a beviteli értékekhez
length = st.slider("Length (cm):", min_value=0.1, max_value=100.0, value=30.0, step=0.1)
width = st.slider("Width (cm):", min_value=0.1, max_value=100.0, value=30.0, step=0.1)
min_piece_size = st.slider("Minimum Piece Size (cm):", min_value=0.1, max_value=20.0, value=5.0, step=0.1)

divisions_length, divisions_width = calculate_divisions(length, width, min_piece_size)
piece_width = width / divisions_width
piece_length = length / divisions_length
st.write(f"Piece size: {piece_length:.2f} cm x {piece_width:.2f} cm")

fig = plot_divisions(length, width, divisions_length, divisions_width)
st.pyplot(fig)
