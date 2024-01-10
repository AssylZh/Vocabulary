from tkinter import *

BACKGROUND_COLOR = "#ADD8E6"

window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/front.png")
canvas.create_image(400, 263, image=front_img)
canvas.create_text(400, 150, text="Title", font=("TkDefaultFont", 40, "italic")) 
canvas.create_text(400, 263, text="Word", font=("TkDefaultFont", 60, "bold"))  

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0)

window.mainloop()
