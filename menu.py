import os
from tkinter import *

from click import open_file


window=Tk()
# add widgets here
window.title('Media Pipe')
window.geometry("300x200+10+10")
#window.geometry("400x400")
bg = PhotoImage( file = 'assets/anime.png')
label1 = Label( window, image = bg)
label1.place(x = 0,y = 0, relwidth = 1, relheight = 1)

#do a function to open the file applyF.py in this directory and run it if the button is clicked 
def open_file():
    #si el boton es Use Filters es presionado, se abre el archivo applyF.py y se ejecuta 
    os.system('python applyF.py')

def faceMeshTest():
    #si el boton es Use Filters es presionado, se abre el archivo applyF.py y se ejecuta 
    os.system('python facemeshTest.py')

btn = Button(window, text="Use Filters", fg='blue', command=open_file)
btn.place(x=80, y=100)
btn=Button(window, text="Use emotions", fg='blue', command=faceMeshTest)
btn.place(x=80, y=150)
lbl=Label(window, text="Main Menu", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
window.mainloop()