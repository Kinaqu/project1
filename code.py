from tkinter import *
from turtle import right
from googletrans import Translator
from matplotlib.pyplot import gray, grid
from pyparsing import anyCloseTag

def transl (): 
    text = abc.get()
    a = translator.translate(text, dest='en')
    bca.delete(0 , END)
    bca.insert(0,a.text)

window = Tk()
window.title("Переводчик")

window.geometry('500x500')

translator = Translator()

    

lbl = Label (window, text="Русский")

btn = Button(window, text = "перевести" , command = transl)

lbl1 = Label (window, text= "Английский") 

abc = Entry(window)  



bca = Entry(window )  


lbl.place(relx=0.2 , y = 30 , anchor=CENTER)
lbl1.place(relx=0.8 , y=30 , anchor=CENTER)


btn.place(relx=0.5 , y = 300 , anchor=CENTER)



abc.place( height = 300 , width=600, relx=0.2 , y=230 , anchor= CENTER  )  
bca.place(height = 300 , width= 600 ,relx=0.8 , y = 230 , anchor= CENTER )  







window.mainloop()
