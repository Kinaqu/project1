from tkinter import *
import requests
from bs4 import BeautifulSoup

window = Tk()

window.title("Переводчик")


    

lbl = Label (window, text="Русский")

btn = Button(window, text = "перевести" )

lbl1 = Label (window, text= "Английский") 

abc = Entry(window,width=20,height=30)  

bca = Entry(window,width=20,height=30)  


lbl.grid(column=0, row=0)
lbl1.grid(column=6, row=0)


btn.grid(column=4, row=5)



abc.grid(column=0, row=3)  
bca.grid(column=6, row=3)  



rs = requests.get('http://www.7english.ru/dictionary.php?id=2000&letter=all')
root = BeautifulSoup(rs.content, 'html.parser')

en_ru_items = []

for tr in root.select('tr[onmouseover]'):
    td_list = [td.text.strip() for td in tr.select('td')]

    if len(td_list) != 9 or not td_list[1] or not td_list[5]:
        continue
    en = td_list[1]




    ru = td_list[5].split(', ')[0]

    en_ru_items.append((en, ru))


window.mainloop()
