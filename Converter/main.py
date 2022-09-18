from curses import window
from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width = 200, height=100)
window.config(padx =20 , pady = 20)


miles_input = Entry(width = 10,)
miles_input.grid(column=2, row = 0)


# Lable
miles_lable = Label(text = "Miles", font=("Ariel", 24, "bold"))
miles_lable.grid(column=3, row = 0)

# Lable
is_equal_lable = Label(text = "is equal to", font=("Ariel", 24, "bold"))
is_equal_lable.grid(column=0, row = 1)

km_result_lable = Label(text = "0", font=("Ariel", 24, "bold"))
km_result_lable.grid(column=2, row = 1)

km_text_lable = Label(text = "KM", font=("Ariel", 24, "bold"))
km_text_lable.grid(column=3, row = 1)

def button_on_click():
    miles_input_value =  miles_input.get()
    converted_km_value = int(miles_input_value)*1.609
    km_result_lable.config(text = converted_km_value)


calculate_button = Button(text =  "Calculate", command=button_on_click)
calculate_button.grid(column=2, row = 3)

window.mainloop()