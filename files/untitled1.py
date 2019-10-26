import tkinter as tk
from PIL import ImageTk, Image

HEIGHT = 500
WIDTH = 500

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


"""path = "back.jpg"

img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(canvas, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")"""


frame = tk.Frame(root, bg='#80c1ff')
frame.place(relwidth=1, relheight=1)

label = tk.Label(frame, text="Welcome to ATTENDANCE 4.0", bg="yellow")
#label.grid(row=0, column=0)
#label.pack(side="top", fill='both')

button = tk.Button(frame, text="Recorgnise", bg='gray', fg='red')
#button.grid(row=1, column=0)
#button.pack(side="top", fill='x')

button = tk.Button(frame, text="Register", bg='gray', fg='red')
button.pack(side="top", fill='both')



#entry = tk.Entry(frame, bg='green')
#entry.pack()

root.mainloop()