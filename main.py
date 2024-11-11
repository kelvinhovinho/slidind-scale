from tkinter import *

def submit():
    print('The temperature is ', scale.get(), 'derees C')

    if (scale.get()<=20) and (scale.get()>=0):
        print("It is to cold,keep warm.")
window = Tk()

scale = Scale(window, from_=100, to=0,
length=600,
# orient=HORIZONTAL
font=('Consolas',20),
tickinterval=10,
showvalue=0,
troughcolor='#69eaff',
fg='#ff1c00',
bg='black',
)
# scale.set(100)
scale.pack()

button = Button(window, text='Submit', command=submit)
button.pack()

window.mainloop()