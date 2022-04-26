from tkinter import *
from password_checker import pc4
from tkinter import ttk


win = Tk()
win.geometry('700x250')


Label(text="Password").grid(row=0)
ent1 = Entry(win)
ent1.grid(column=1,row=0)
var = StringVar()

testing = False
def get_content():
    checker = pc4.PasswordChecker(ent1.get())


    if(checker.isvulnerable()):
        Label(text="Weak").grid(column=4,row=0)

        
    else:
        Label(text="Strong").grid(column=4,row=0)
        # generate password
        # would you like to generate a new password?
   

        

def ask_to_generate():
    new_win = Tk()
    new_win.geometry('700x250')
    the_rules = Label(new_win,text="Enter length of password")
    the_rules.grid(row=0)
    e = Entry(new_win)
    e.grid(column=1,row=0)


# Todo
# When weak generate password 


btn = Button(win, text="Test password", width=15,height=1,command=get_content)
btn.place(x=60,y=30)
b1 = ttk.Button(win, text= "Generate Password?",command=ask_to_generate)
b1.place(x=60,y=70)


   




mainloop()
