from tkinter import *
from time import strftime
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

#------- display time on the canvas -------

data = pd.read_csv("new_qoutes.csv")
dict_data = data.to_dict(orient="records")


def time():
	global time_reseter

	root.after_cancel(time_reseter)
	string_2 = strftime('%a, %d %b %Y')
	string = strftime('%H:%M:%S %p')
	canvas.itemconfig(date, text=string_2)
	canvas.itemconfig(clock, text = string)
	time_reseter = root.after(1000, time)


def back_to_clock():
	canvas.itemconfig(background_img, image=green_img)
	canvas.itemconfig(message, text="")


def qoutes():
	randomised_data = random.choice(dict_data)
	canvas.itemconfig(background_img, image=white_img)
	author = randomised_data['Author']
	qoute = randomised_data['Quote']
	canvas.itemconfig(message, text=f"{qoute}\n\n~{author}~")


#------- tkinter window ----------
root = Tk()
root.title('Clock')
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
time_reseter = root.after(1000, func=time)

#------- Ui setup: Canvas --------
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
green_img = PhotoImage(file="card_back.png")
white_img = PhotoImage(file="card_front.png")
background_img = canvas.create_image(400, 263,image=green_img)
date = canvas.create_text(400, 150, text="Digital World", font=("Ariel", 40, "italic"), fill="white")
clock = canvas.create_text(400, 265, text="", font=("Ariel", 60, "bold"), fill="white")
message = canvas.create_text(400, 200, text="", font=("Ariel", 20, "bold"), fill="black", width=400, anchor="center")
canvas.grid(row=0, column=0, columnspan=2)


#-------- x button --------
cross_image = PhotoImage(file="wrong.png")
x_button = Button(image=cross_image, bd=0, highlightthickness=0, command=back_to_clock)
x_button.grid(row=1, column=0)

#-------- y button ---------
check_image = PhotoImage(file="right.png")
y_button = Button(image=check_image,bd=0, highlightthickness=0, command=qoutes)
y_button.grid(row=1, column=1)

time()



mainloop()
