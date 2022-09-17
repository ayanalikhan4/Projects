from curses import window
import tkinter

window = tkinter.Tk()
window.title("My first GUI Progame")
window.minsize(width = 500, height=300)

my_lable = tkinter.Label(text = "I am a lable", font=("Ariel", 24, "bold"))
my_lable.pack()


window.mainloop()