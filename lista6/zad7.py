from tkinter import *
from tkinter import ttk
import random
import time
 
def insertion_sort(array, drawData, time_tick):
    """Algorytm sortowania przez wstawianie."""

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
            drawData(data)
            time.sleep(time_tick)
        
        array[j+1] = key
        drawData(data)
        time.sleep(time_tick)

root = Tk()
root.title("Insertion sort Visualizer")

root.maxsize(1600, 1024)
root.config(bg="Black")
select_alg = StringVar()
data = []

def generate():
    """Generuje tablicę losowych 15 liczb z zakresu od 1 do 100"""

    global data
    sizeval = 15
    data = []
    for i in range(sizeval):
        data.append(random.randint(1,100))

    drawData(data)


def drawData(data):
    """Tworzy słupki odpowiadające liczbą z tablicy."""

    canvas.delete("all")
    bar_height = 500
    bar_width = 800
    x_width = bar_width/(len(data) + 1)
    offset = 125
    spacing = 20

    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        
        x0 = i*x_width + offset + spacing
        y0 = bar_height - height *  400 
        x1 = ((i*1)*x_width) + offset
        y1 = bar_height
        
        canvas.create_rectangle(x0, y0, x1, y1, fill = "Blue")
        canvas.create_text(x0+2, y0, anchor=SE, text=str(data[i]))
    root.update_idletasks()

def alogrithm():
    """Wizualizacja algorytmu sortowania przez wstawianie."""
    global data
    insertion_sort(data, drawData, 0.05)

mainframe = Frame(root, width=1000, height=50, bg="Grey")
mainframe.grid(row=1, column=0)

Generate = Button(mainframe, text="Generate", bg="Red", command=generate)
Generate.place(height=40, width=300, x = 25, y = 5)

start = Button(mainframe, text="START", bg="Blue", command=alogrithm)
start.place(height=40, width=300, x = 675, y = 5)

canvas = Canvas(root, width=1000, height=600, bg="White")
canvas.grid(row=0, column=0)

root.mainloop()