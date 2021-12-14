from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(letters) for _ in range(randint(2, 4))]

    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)

    password="".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_value = website_entry.get()
    email_value = email_entry.get()
    password_value = password_entry.get()
    if len(website_value)==0 or len(password_value)==0:
        messagebox.showinfo(title="Oops", message="Please make sure you have filled all the fields")
    else:

        is_ok = messagebox.showinfo(title=website, message=f"These are the details entered: \nEmail:{email_value}\n password:{password_value}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_value}|{email_value}|{password_value}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #
from tkinter import Button

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#labels
website = Label(text="Website")
website.grid(row=1, column=0)
email = Label(text="Email/Username")
email.grid(row=2, column=0)
password_label = Label(text="password")
password_label.grid(row=3, column=0)

#entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "1234@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#button
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command= save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()