from fnmatch import translate
from tkinter import *
from turtle import right
from googletrans import Translator
from matplotlib import image
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
import smtplib

my_email = "tr4ns1atordm@gmail.com"
password = "Translate123"


pyt.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'



def transl (): 
    text = abc.get(1.0 , END)
    a = translator.translate(text, dest='en')
    bca.delete(1.0 , END)
    bca.insert(1.0,a.text)

def openfile():
    path = askopenfilename()
    image =Image.open(path)
    img=ImageTk.PhotoImage(image)
    view.create_image(5,10, image=img, anchor=NW)

def Translate():
    path = askopenfilename()
    image1 =Image.open(path)
    string = pyt.image_to_string(image1)
    res = translator.translate(string, dest = 'ru')
    cda.delete(1.0 , END)
    cda.insert(1.0, res.text)

 
def sender ():
    email = entr.get()
    message = sts.get(1.0 , END)
    em="tr4ns1atordm@gmail.com"
    pw= "dftcdzlecclqtyyt"
    connection = smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user=em , password = pw)
    connection.sendmail(from_addr = em , to_addrs = email , msg=(message,"с уважением DMTransl") )
    connection.close()
    


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

button2_tab2 = Button(tab2 , text = "Перевести" , command = translate)

button2_tab2.place(relx=0.3 , y= 40 , anchor = CENTER)

cda = scrolledtext.ScrolledText(tab2)
cda.place( height = 300 , width=600, relx=0.7 , y=230 , anchor= CENTER  )  

view = Canvas(tab2)
view.place( width=600, height=300,relx=0.1,y = 90 )



lbl_tab3 = Label (tab3, text= "Введите адрес получателя") 

lbl_tab3.place(relx=0.2 , y=30 , anchor=CENTER)


entr = Entry(tab3)
entr.place( height = 60 , width=200, relx=0.2 , y=130 , anchor= CENTER  )  


lbl2_tab3 = Label (tab3, text= "Введите сообщение") 

lbl2_tab3.place(relx=0.7 , y= 150, anchor=CENTER)

sts = scrolledtext.ScrolledText(tab3)
sts.place( height = 200 , width=500, relx=0.7 , y=300 , anchor= CENTER  )  



button_tab3 = Button(tab3 , text = "Отправить сообщение" , command = sender)

button_tab3.place(relx=0.7 , y= 500 , anchor = CENTER)



tab_control.pack(expand=1, fill='both') 
window.mainloop()