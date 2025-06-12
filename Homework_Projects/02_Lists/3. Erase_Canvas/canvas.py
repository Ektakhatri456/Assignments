# Program 3: Canvas Eraser

#Implement an 'eraser' on a canvas.
#The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. 
# We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

import tkinter as tk

Canvas_width = 800
Canvas_height = 800
Cell_size = 20
Eraser_size = 20

mouse_x = 0
mouse_y = 0
mouse_pressed = False

def main():
    global mouse_x, mouse_y, mouse_pressed
    root = tk.Tk()
    root.title("Canvas Eraser - Drag to erase")
    canvas = tk.Canvas(root, width=Canvas_width, height=Canvas_height)
    canvas.pack()

    # For creating blue canvas grid
    for row in range(0, Canvas_height, Cell_size):
        for col in range(0, Canvas_width, Cell_size):
            canvas.create_rectangle(col, row, col + Cell_size, row + Cell_size, fill="blue", outline="black")

    eraser = canvas.create_rectangle(0, 0, Eraser_size, Eraser_size, fill="pink")

    def update_mouse_position(event):
        global mouse_x, mouse_y
        mouse_x = event.x
        mouse_y = event.y

    def set_mouse_pressed(event):
        global mouse_pressed
        mouse_pressed = True

    def set_mouse_released(event):
        global mouse_pressed
        mouse_pressed = False

    def erase_canvas():
        if not mouse_pressed:
            return
        overlap = canvas.find_overlapping(mouse_x, mouse_y, mouse_x + Eraser_size, mouse_y + Eraser_size)
        for item in overlap:
            if item != eraser:
                canvas.itemconfig(item, fill="white")

    def move_eraser():
        canvas.coords(eraser, mouse_x, mouse_y, mouse_x + Eraser_size, mouse_y + Eraser_size)
        erase_canvas()
        root.after(30, move_eraser)

    # Bindings
    canvas.bind("<Motion>", update_mouse_position)
    canvas.bind("<ButtonPress-1>", set_mouse_pressed)
    canvas.bind("<ButtonRelease-1>", set_mouse_released)

    move_eraser()
    root.mainloop()

if __name__ == "__main__":
    main()