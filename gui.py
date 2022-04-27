from copy import copy
from tkinter import *
from tkinter.ttk import *
from password_checker import pc4
from password_strength import PasswordPolicy
from PIL import ImageTk, Image


import array
import random
import pyperclip


policy = PasswordPolicy.from_names(
    strength=0.66  # need a password that scores at least 0.5 with its strength
)



# Determining whether a password is weak or strong
def get_content():
    
    tested_pass = policy.password(ent1.get())
    
    if(tested_pass.strength() >= 0.0 and tested_pass.strength() < .5):
        Label(text="Weak").place(x=70,y=30)
    elif(tested_pass.strength() >= .5 and tested_pass.strength() < .66):
        Label(text="Good").place(x=70,y=30)
    else:
        Label(text="Strong").place(x=70,y=30)

   

def random_character(a):

    character_list = list(a)
    # random.randrange(len(character_list))
    random_char = character_list[random.randrange(len(character_list))]

    return random_char


def generate_password():
    
    
    password_length = var1.get()

    password = ""

    alphabet_lc = "abcdefghijklmnopqrstuvwxyz"
    alphabet_uc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_characters = "`!@#$%^&*()-_+=[]|;:<>,./?"
        
    for x in range(password_length):

     random_number = random.randrange(1,5)

     if random_number == 1:
         password += random_character(alphabet_lc) 
     elif random_number == 2:
         password += random_character(alphabet_uc)
     elif random_number == 3:
         password += random_character(numbers)
     elif random_number == 4:
         password += random_character(special_characters)


    password_list = array.array('u', password)
    

    test = ""
    for y in password_list:
        test += y

    
    return test


def password_generated():
    gen_e.delete(0,END)
    new_pass = generate_password()
    gen_e.insert(10,new_pass)


def copy_password():
    pyperclip.copy(gen_e.get())
    


# Window creation
win = Tk()
win.geometry("500x200")


img = PhotoImage(file='shrek.png')
Label(
    win,
    image=img
).place(x=0,y=0)

# Testing password creation
Label(text="Password").grid(row=0)
ent1 = Entry(win)
ent1.grid(column=1,row=0)


# Length label for generated password
c_label = Label(win, text="Length")
c_label.place(x=0,y=100)

# Combobox creation
var1 = IntVar()
combo = Combobox(win, textvariable=var1)

 
# Combo Box for length of your password
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32)
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.place(x=50,y=100)

# Generate password label
generated_password = Label(win, text="Generated password")
generated_password.place(x=0,y=130)

# Entry where generated password goes
gen_e = Entry(win)
gen_e.place(x=110,y=130)

# Generate password button
b1 = Button(win, text= "Generate Password",command=password_generated)
b1.place(x=200,y=100)

# Copy button
# This button will allow the user to copy the generated password so they can test it afterwards
copy_btn = Button(win, text="Copy",command=copy_password)
copy_btn.place(x=240,y=130)


# Testing password button
btn = Button(win, text="Test password",command=get_content)
btn.place(x=200,y=0)




mainloop()
