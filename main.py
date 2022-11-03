import os
from tkinter import *

window=Tk()

window.title('Media Pipe')
window.geometry("300x200")

bg = PhotoImage( file = 'assets/background.png')

label1 = Label( window, image = bg)
label1.place(x = 0,y = 0, relwidth = 1, relheight = 1)
def recongEmotion():
    os.system('python EmotionRecognition/main.py')

def applyF():
    os.system('python applyF.py')

def faceMeshTest():
    os.system('python facemeshTest.py')

def openNewWindowF():
    newWindow = Toplevel(window)
    newWindow.title('Filters')
    newWindow.geometry("300x200+10+10")

    label1 = Label( newWindow, image = bg)
    label1.place(x = 0,y = 0, relwidth = 1, relheight = 1)

    lbl=Label(newWindow, text="Filters", fg='#6F02BD' , font=("Helvetica", 16))
    lbl.place(x=60, y=50)
    btn = Button(newWindow, text = 'Apply Filters', bg='#BDBD52' ,command = applyF, font=("Helvetica", 10), fg='#3B3E70')
    btn.place(x = 80, y = 100)
    btn=Button(newWindow, text="Face Mesh Test ", bg='#BDBD52', command=faceMeshTest, font=("Helvetica", 10), fg='#3B3E70')
    btn.place(x=80, y=150)


btn = Button(window, text="Filters", fg='#003621', font=("Helvetica", 12), bg='#F5675D', command=openNewWindowF, borderwidth=3, relief="raised")
btn.place(x=120, y=30)
btn = Button(window, text="Emotion Recognition", fg='#159428', font=("Helvetica", 12), bg='#B8B45C', command=recongEmotion, borderwidth=3, relief="raised")
btn.place(x=70, y=70)
lbl=Label(window, text="Main Menu", fg='#36341B', font=("Helvetica", 18), bg='#f8f8f8')
lbl.place(x=90, y=145)
window.mainloop()