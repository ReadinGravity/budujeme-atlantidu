import tkinter as tk
import random

# Constants
IMAGE_PATH = "../img/"  # Path to the image files

# Global variables
empty = []
coin_count = 0
most = []
button = None  # Define button as a global variable
coins = None  # Define coins as a global variable

def setup():
    global empty, coin_count, most, button, coins  # Add coins to global variables
    empty = []
    for x in range(0, WIDTH - 3 * square, square):
        for y in range(0, HEIGHT, square):
            if random.randrange(0, 100) < 20:
                canvas.create_image(x, y, image=ostrov0, anchor=tk.NW)
            else:
                empty.append(canvas.create_image(x, y, image=ostrov3, anchor=tk.NW))
    coins = canvas.create_text(WIDTH - 3 * square, 0, text=coin_count, font=('Helvetica', '30', 'bold'), anchor=tk.NW)
    button = canvas.create_image(WIDTH - square, 0, image=ostrov_kruh0, anchor=tk.NW)

def click(event):
    global empty, coin_count, most
    clicked = canvas.find_overlapping(event.x, event.y, event.x + 1, event.y + 1)
    if button in clicked:
        change_button()
    elif clicked and clicked[0] in empty:
        canvas.itemconfig(clicked[0], image=change_island(clicked[0]))
        empty.remove(clicked[0])
    elif clicked and clicked[0] in most:
        item_image = canvas.itemcget(clicked[0], 'image')
        if item_image == str(ostrov1):
            canvas.itemconfig(clicked[0], image=ostrov2)
        elif item_image == str(ostrov2):
            canvas.itemconfig(clicked[0], image=ostrov1)


def change_button():
    if canvas.itemcget(button, 'image') == str(ostrov_kruh1):
        canvas.itemconfig(button, image=ostrov_kruh0)
    else:
        canvas.itemconfig(button, image=ostrov_kruh1)

def change_island(ff):
    global coin_count
    if canvas.itemcget(button, 'image') == str(ostrov_kruh1):
        coin_count += 50
        canvas.itemconfig(coins, text=str(coin_count))
        return ostrov0
    else:
        coin_count += 10
        canvas.itemconfig(coins, text=str(coin_count))
        most.append(ff)
        return ostrov1

M = random.randint(4, 6)
N = random.randint(3, 9)

root = tk.Tk()
square = 50
WIDTH = square * (M + 3)
HEIGHT = square * N
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# Load images
ostrov0 = tk.PhotoImage(file=IMAGE_PATH + 'ostrov0.png')
ostrov1 = tk.PhotoImage(file=IMAGE_PATH + 'ostrov1.png')
ostrov2 = tk.PhotoImage(file=IMAGE_PATH + 'ostrov2.png')
ostrov3 = tk.PhotoImage(file=IMAGE_PATH + 'ostrov3.png')
ostrov_kruh0 = tk.PhotoImage(file=IMAGE_PATH + 'ostrov_kruh0.png')
ostrov_kruh1 = tk.PhotoImage(file=IMAGE_PATH + 'ostrov_kruh1.png')

setup()
canvas.bind('<Button-1>', click)

root.mainloop()
