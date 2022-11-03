import os
from tkinter import *

window=Tk()

window.title('Media Pipe')
window.geometry("300x200")

# bg = PhotoImage( file = 'assets/anime.png')

# label1 = Label( window, image = bg)
# label1.place(x = 0,y = 0, relwidth = 1, relheight = 1)
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

    lbl=Label(newWindow, text="Filters", fg='#57DCF7' , font=("Helvetica", 16))
    lbl.place(x=60, y=50)
    btn = Button(newWindow, text = 'Apply Filters', fg='red' ,command = applyF)
    btn.place(x = 80, y = 100)
    btn=Button(newWindow, text="Face Mesh Test ", fg='blue', command=faceMeshTest)
    btn.place(x=80, y=150)


btn = Button(window, text="Filters", fg='blue', command=openNewWindowF)
btn.place(x=80, y=100)
btn = Button(window, text="Emotion Recognition", fg='red', command=recongEmotion)
btn.place(x=80, y=150)
lbl=Label(window, text="Main Menu", fg='#57DCF7', font=("Helvetica", 16))
lbl.place(x=60, y=50)
window.mainloop()