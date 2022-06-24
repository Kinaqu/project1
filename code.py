from tkinter import *
from turtle import right
from googletrans import Translator
from matplotlib.pyplot import gray, grid
from pyparsing import anyCloseTag
from tkinter import scrolledtext
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pytesseract as pyt
import cv2
import matplotlib.pyplot as plt
from PIL import *
from PIL import Image , ImageTk





def transl (): 
    text = abc.get(1.0 , END)
    a = translator.translate(text, dest='en')
    bca.delete(1.0 , END)
    bca.insert(1.0,a.text)

def openfile():
    path = askopenfilename()
    image = ImageTk.PhotoImage(Image.open(path))
    view.create_image(5,10, image=image, anchor=NW)

    imag = cv2.imread(path)
    string = pyt.image_to_string(imag)
    res = translator.translate(string, dest = 'ru')
    print(string)
    cda.delete(1.0 , END)
    cda.insert(1.0, res.string)

    


window = Tk()
tab_control = ttk.Notebook(window)

window.title("Переводчик")

window.geometry('500x500')

translator = Translator()


tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control) 

tab_control.add(tab1, text='Перевод текста')
tab_control.add(tab2, text='Фотоперевод') 
tab_control.add(tab3, text='Сохранить,поделиться') 

    

lbl = Label (tab1, text="Русский")

btn = Button(tab1, text = "перевести" , command = transl)

lbl1 = Label (tab1, text= "Английский") 

abc = scrolledtext.ScrolledText(tab1)  
bca = scrolledtext.ScrolledText(tab1)  

lbl.place(relx=0.2 , y = 30 , anchor=CENTER)
lbl1.place(relx=0.8 , y=30 , anchor=CENTER)
btn.place(relx=0.5 , y = 300 , anchor=CENTER)

abc.place( height = 300 , width=600, relx=0.2 , y=230 , anchor= CENTER  )  
bca.place(height = 300 , width= 600 ,relx=0.8 , y = 230 , anchor= CENTER )  




button_tab2 = Button(tab2 , text = "Загрузить файл" , command = openfile)

button_tab2.place(relx=0.1 , y= 40 , anchor = CENTER)



cda = scrolledtext.ScrolledText(tab2)
cda.place( height = 300 , width=600, relx=0.7 , y=230 , anchor= CENTER  )  

view = Canvas(tab2)
view.place( width=600, height=300,relx=0.1,y = 90 )



tab_control.pack(expand=1, fill='both') 
window.mainloop()