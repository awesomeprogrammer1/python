from tkinter import *
root = Tk()


root.geometry('500x350')
root.title('SignIn')

myLogin = 'andrew'
myPass  = 'abc'
count = 0

a= Label(text = 'Welcome', font= ('Verdana', 16))
a.pack()

c= Label(text = '\nEnter Your Login', font= ('Verdana', 12))
c.pack()

userLogin= Entry()
userLogin.pack()

d= Label(text = '\nEnter Your Password', font= ('Verdana', 12))
d.pack()

userPass = Entry()
userPass.pack()

space = Label(text = ' ', font= ('Verdana', 14))
space.pack()

def sign():
    global count
    if userLogin.get() == myLogin and userPass.get() == myPass:
        e = Label(text = '\nSuccessfully logged in', fg = 'green', font = ('Verdana',16))
        e.pack()
        userLogin.config(state = DISABLED)
        userPass.config(state= DISABLED)
        btn.config(state= DISABLED)
    else:
        f = Label(text = '\nPassword or Username Invalid', fg = 'red', font = ('Verdana',16))
        f.pack()
        count+=1
        if count == 3:
            userLogin.config(state = DISABLED)
            userPass.config(state= DISABLED)
            btn.config(state= DISABLED)



btn = Button(text='Login', command = sign, width = 10)
btn.pack()























































root.mainloop()