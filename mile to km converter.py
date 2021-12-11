from tkinter import *

def miles_to_km():
    miles = float(input.get())
    km = miles*1.609
    result.config(text=f"{km}")

window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=200)
window.config(padx=50, pady=50)

input = Entry(width=20, text="0")
print(input.get())
input.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

label4 = Label(text="km")
label4.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)
window.mainloop()