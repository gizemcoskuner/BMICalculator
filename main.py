from tkinter import *

window = Tk()
window.title = ("BMI Calculator")
window.minsize(width=300, height=300)
window.config(padx=30, pady=30)

weight_label = Label(text="Enter Your Weight (kg)")
weight_label.config(padx=10, pady=10)
weight_label.pack()

weight_entry = Entry(width=15)
weight_entry.pack()

height_label = Label(text="Enter Your Height (cm)")
height_label.config(padx=10, pady=10)
height_label.pack()

height_entry = Entry(width=15)
height_entry.pack()

def button_clicked():
    try:
        weight = int(weight_entry.get())
        height = (int(height_entry.get()) / 100)
        bmı = float("{:.2f}".format(weight / height ** 2))

        if bmı <= 18.5:
            calculation_label = Label(text=f"Your BMI is {bmı}. You are under weight.")
            calculation_label.place(x=20, y=170)
        if 18.5 < bmı <= 24.9:
            calculation_label = Label(text=f"Your BMI is {bmı}. You are normal weight.")
            calculation_label.place(x=20, y=170)
        if 24.9 < bmı <= 29.9:
            calculation_label = Label(text=f"Your BMI is {bmı}. You are over weight.")
            calculation_label.place(x=20, y=170)
        if 29.9 < bmı <= 39.9:
            calculation_label = Label(text=f"Your BMI is {bmı}. You are obese.")
            calculation_label.place(x=20, y=170)
        if 39.9 < bmı:
            calculation_label = Label(text=f"Your BMI is {bmı}. You are extreme obese.")
            calculation_label.place(x=20, y=170)


    except:
        if weight_entry != int:
            value_label = Label(text="Please enter a valid number.")
            value_label.place(x=50, y=170)

        if height_entry != int:
            value_label = Label(text="Please enter a valid number.")
            value_label.place(x=50, y=170)


calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.place(x=90, y=135)

window.mainloop()