import tkinter

window = tkinter.Tk()

window.title("Unit Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# # Label
# label = tkinter.Label(text="Unit Converter", font=("Arial", 20, "bold"))
# label.grid(column=1, row=1)
#
#
# def clicked():
#     text = input.get()
#     label.config(text=text)
#     print("Clicked...")
#
#
# # button
# btn = tkinter.Button(text="Click Me", command=clicked)
# btn.grid(column=2, row=2)
#
# btn2 = tkinter.Button(text="NewBtn", command=clicked)
# btn2.grid(column=3, row=1)
#
# # entry
# input = tkinter.Entry()
# input.grid(column=4, row=3)

label1 = tkinter.Label(text="is equal to")
label1.grid(column=1, row=2)

input_val = tkinter.Entry(width=7)
input_val.grid(column=2, row=1)

label2 = tkinter.Label(text="Miles")
label2.grid(column=3, row=1)

label3 = tkinter.Label(text="0")
label3.grid(column=2, row=2)

label4 = tkinter.Label(text="Km")
label4.grid(column=3, row=2)


def clicked():
    print("Clicked...")
    miles = input_val.get()
    km = float(miles) * 1.609
    label3.config(text=km)


btn = tkinter.Button(text="Calculate", command=clicked)
btn.grid(column=2, row=3)

window.mainloop()
