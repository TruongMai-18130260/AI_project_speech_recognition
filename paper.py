from tkinter import *
from datetime import datetime
import random
import re
from tkinter import messagebox
from tkinter.font import Font
import textwrap
import json 

# root = Tk()
# root.config(bg="#fa3c4c")
# root.geometry('410x600+400+100')

# #ana ekran
# canvas = Canvas(root, width=200, height=200,bg="white")
# canvas.grid(row=0,column=0,columnspan=2)
# canvas.place(x=10, y=10, width=390, height=530)

# bubbles = []
# jo = []
# bubbles1 = []

# class BotBubbleAgent:
#     def __init__(self,master,message=""):
#         self.master = master
#         self.frame = Frame(master,bg="#e4e6eb")
#         self.i = self.master.create_window(73,490,window=self.frame)       
#         Label(self.frame,text="AGENT |"+datetime.now().strftime("%d-%m-%Y %X"),fg="#8A8D91",font=("sans-serif", 7),bg="#e4e6eb").grid(row=0,column=0,sticky="w",padx=5) #tarih saat        
#         Label(self.frame, text=textwrap.fill(message, 15),justify="left",fg="#050505", font=("sans-serif", 9),bg="#e4e6eb").grid(row=1, column=0,sticky="w",padx=5,pady=3)
#         root.update_idletasks()
#     #     self.master.create_polygon(self.draw_triangle(self.i), fill="#e4e6eb", outline="#e4e6eb")



#     # def draw_triangle(self,widget):
#     #     x1, y1, x2, y2 = self.master.bbox(widget)
#     #     return x1, y2 - 10, x1 - 15, y2 + 10, x1, y2

# class BotBubbleUser:
#         def __init__(self,master,message=""):
#             self.master = master
#             self.frame = Frame(master,bg="#fa3c4c")
#             self.i = self.master.create_window(320,490,window=self.frame)       
#             Label(self.frame,text="USER |"+datetime.now().strftime("%d-%m-%Y %X"),fg="white smoke",font=("sans-serif", 7),bg="#fa3c4c").grid(row=0,column=0,sticky="w",padx=5) #tarih saat        
#             Label(self.frame, text=textwrap.fill(message, 15),justify="left",fg="#fff", font=("sans-serif", 9),bg="#fa3c4c").grid(row=1, column=0,sticky="w",padx=5,pady=3)
#             root.update_idletasks()
#         #     self.master.create_polygon(self.draw_triangle(self.i), fill="#fa3c4c", outline="#fa3c4c")



#         # def draw_triangle(self,widget):
#         #     x1, y1, x2, y2 = self.master.bbox(widget)
#         #     return x1, y2 + 10, x1 + 15, y2 - 10, x1, y2

# def send_message():
#     if bubbles:
#         canvas.move(ALL, 0, -30) 
    
#     tmp = entry.get()
#     a = BotBubbleUser(canvas,message=tmp)
#     bubbles.append(a)
#     send_message1(tmp)
#     print(bubbles)
    
        
# def send_message1(tmp):
#     tmp = tmp.lower()
#     with open("exampledata.json", "r") as outfile: 
#         jo = json.load(outfile)
    
#     for x in jo:
#         if bubbles:
#             canvas.move(ALL, 0, -30) 
#         if x["question"] == tmp:
#             b = BotBubbleAgent(canvas,message=x["answer"])
#             bubbles1.append(b)

    

# entry = Entry(root,width=26, font=("sans-serif", 10))
# entry.place(x=10, y=550, width=290, height=40)


# #buton
# buton = Button(root, width=10, height=2, 
# relief='raised',state='active',command=send_message)
# buton.config(text='SEND', bg='#e4e6eb', font='sans-serif 8 bold')
# buton.place(x=310, y=550)

# root.mainloop()

with open("exampledata.json", "r") as outfile:
    tmp = json.dumps(json.load(outfile))
    data = tmp[1:len(tmp)-1]
    print(data)    