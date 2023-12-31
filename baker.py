import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as patches

# Globális változók a figure és axis tárolásához
fig, ax = plt.subplots()
fig.set_facecolor('#343444')  # Háttérszín beállítása a plotnak
ax.set_facecolor('#343541')  # Háttérszín beállítása az axes-nek

def calculate_divisions(length, width, min_piece_size):
    """
    Calculates the number of divisions along the length and width of the dough
    to achieve as uniform pieces as possible, considering a minimum piece size.

    :param length: Length of the dough in cm.
    :param width: Width of the dough in cm.
    :param min_piece_size: Minimum size of one side of a piece in cm.
    :return: A tuple of (number of divisions along length, number of divisions along width).
    """

    # Calculating the number of divisions along length and width
    divisions_length = max(1, int(length // min_piece_size))
    divisions_width = max(1, int(width // min_piece_size))

    return divisions_length, divisions_width

def update_plot():
    length = float(length_entry.get())
    width = float(width_entry.get())
    min_piece_size = slider.get()
    divisions_length, divisions_width = calculate_divisions(length, width, min_piece_size)
    plot_divisions(length, width, divisions_length, divisions_width)

def plot_divisions(length, width, divisions_length, divisions_width):
    ax.clear()  # Töröljük a korábbi tartalmat
    ax.set_facecolor('#343541')  # Minden tisztítás után újra be kell állítani az axes háttérszínét
    rectangle = patches.Rectangle((0, 0), length, width, edgecolor='#059b76', facecolor="none")
    ax.add_patch(rectangle)
    for i in range(1, divisions_length):
        ax.plot([i * length / divisions_length, i * length / divisions_length], [0, width], color='#c22b6c')
    for j in range(1, divisions_width):
        ax.plot([0, length], [j * width / divisions_width, j * width / divisions_width], color='#c22b6c')
    ax.set_xlim(0, length)
    ax.set_ylim(0, width)
    ax.set_aspect('equal', adjustable='box')
    canvas.draw()

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as patches

def calculate_divisions(length, width, min_piece_size):
    """
    Calculates the number of divisions along the length and width of the dough
    to achieve as uniform pieces as possible, considering a minimum piece size.

    :param length: Length of the dough in cm.
    :param width: Width of the dough in cm.
    :param min_piece_size: Minimum size of one side of a piece in cm.
    :return: A tuple of (number of divisions along length, number of divisions along width).
    """

    # Calculating the number of divisions along length and width
    divisions_length = max(1, int(length // min_piece_size))
    divisions_width = max(1, int(width // min_piece_size))

    return divisions_length, divisions_width

def update_plot():
    try:
        length = float(length_entry.get())
        width = float(width_entry.get())
        min_piece_size = slider.get()
        divisions_length, divisions_width = calculate_divisions(length, width, min_piece_size)

        # Clearing and updating the plot
        ax.clear()
        rectangle = patches.Rectangle((0, 0), length, width, edgecolor='r', facecolor="none")
        ax.add_patch(rectangle)

        # Drawing the dividing lines
        for i in range(1, divisions_length):
            ax.plot([i * length / divisions_length, i * length / divisions_length], [0, width], 'r-')
        for j in range(1, divisions_width):
            ax.plot([0, length], [j * width / divisions_width, j * width / divisions_width], 'r-')

        ax.set_xlim(0, length)
        ax.set_ylim(0, width)
        ax.set_aspect('equal', adjustable='box')
        canvas.draw()
    except ValueError:
        print("Please enter valid numbers for length and width.")

# Ablak létrehozása
window = tk.Tk()
window.title("Baker's Design Calculator")

# Ablak méretének és pozíciójának beállítása
window.geometry('1000x700')  # Növelt kezdő méret

# A fő konténer létrehozása
main_frame = ttk.Frame(window)
main_frame.pack(fill='both', expand=True)

# Grid konfiguráció a fő konténerben
main_frame.columnconfigure(1, weight=3)  # A beviteli mező oszlopának súlyát növeljük


# Méret beviteli mezők
length_label = tk.Label(main_frame, text="Length (cm):")
length_label.grid(row=0, column=0, sticky='ew')
length_entry = tk.Entry(main_frame)
length_entry.grid(row=0, column=1, sticky='ew')

width_label = tk.Label(main_frame, text="Width (cm):")
width_label.grid(row=1, column=0, sticky='ew')
width_entry = tk.Entry(main_frame)
width_entry.grid(row=1, column=1, sticky='ew')

# Csúszka a minimális darab méretéhez, most már lebegőpontos értékekkel is
slider_label = tk.Label(main_frame, text="Minimum Piece Size (cm):")
slider_label.grid(row=2, column=0, sticky='ew')
slider = tk.Scale(main_frame, from_=0.1, to=10, resolution=0.1, orient='horizontal', command=lambda x: update_plot())
slider.grid(row=2, column=1, sticky='ew')

# Ábra hozzáadása a canvas widget segítségével
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=main_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=3, column=0, columnspan=2, sticky='nsew')

# A grid sorainak és oszlopainak konfigurációja, hogy megfelelően skálázódjanak
main_frame.rowconfigure(3, weight=1)
main_frame.columnconfigure(1, weight=1)

# Az ablak futtatása
window.mainloop()