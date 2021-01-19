
from tkinter import *
from datetime import datetime
import random
import re
from tkinter import messagebox
from tkinter.font import Font
import textwrap
import json 
from tkinter import ttk
import tkinter.scrolledtext as ScrolledText
import speak as speakagent

def initFrame():
    root = Tk()
    root.title("TỬ VI CHATBOT")
    root.config(bg="#b42025")
    root.geometry('1020x600+400+100')

    #ana ekran
    canvas = Canvas(root, width=2000, height=200,bg="white")
    canvas.grid(row=0,column=0,columnspan=2)
    canvas.place(x=10, y=10, width=1000, height=530)

    yscrollbar = ttk.Scrollbar(canvas,orient="vertical",command=canvas.yview)
    yscrollbar.pack(side=RIGHT, fill="y")
    canvas.configure(yscrollcommand=yscrollbar.set)
    canvas.bind('<Configure>',lambda e: canvas.configure(scrollregion = canvas.bbox('all')))


    bubbles = []
    jo = []
    bubbles1 = []

    class BotBubbleAgent:
        def __init__(self,master,message=""):
            self.master = master
            self.frame = Frame(master,bg="#e4e6eb",width=50)
            self.i = self.master.create_window(300,490,window=self.frame)       
            Label(self.frame,text="AGENT |"+datetime.now().strftime("%d-%m-%Y %X")+"                      ",fg="#8A8D91",font=("sans-serif", 7),bg="#e4e6eb").grid(row=0,column=0,sticky="w",padx=5) #tarih saat        
            Label(self.frame, text=textwrap.fill(message, 50),justify="left",fg="#050505", font=("sans-serif", 9),bg="#e4e6eb").grid(row=1, column=0,sticky="w",padx=5,pady=3)
            root.update_idletasks()
            


           
        #     self.master.create_polygon(self.draw_triangle(self.i), fill="#e4e6eb", outline="#e4e6eb")



        # def draw_triangle(self,widget):
        #     x1, y1, x2, y2 = self.master.bbox(widget)
        #     return x1, y2 - 10, x1 - 15, y2 + 10, x1, y2

    class BotBubbleUser:
            def __init__(self,master,message=""):
                self.master = master
                self.frame = Frame(master,bg="#fa3c4c")
                
                self.i = self.master.create_window(900,490,window=self.frame)       
                Label(self.frame,text="USER |"+datetime.now().strftime("%d-%m-%Y %X"),fg="white smoke",font=("sans-serif", 7),bg="#fa3c4c").grid(row=0,column=0,sticky="w",padx=5) #tarih saat        
                Label(self.frame, text=textwrap.fill(message, 15),justify="left",fg="#fff", font=("sans-serif", 9),bg="#fa3c4c").grid(row=1, column=0,sticky="w",padx=5,pady=3)
                root.update_idletasks()
            #     self.master.create_polygon(self.draw_triangle(self.i), fill="#fa3c4c", outline="#fa3c4c")



            # def draw_triangle(self,widget):
            #     x1, y1, x2, y2 = self.master.bbox(widget)
            #     return x1, y2 + 10, x1 + 15, y2 - 10, x1, y2


    def send_message2():
        tmp = speakagent.hearme()
        # new_text = "new text"
        v.set(tmp)
        print(tmp)

    def send_message():
        if bubbles:
            canvas.move(ALL, 0, -10) 
        
        tmp = entry.get()
        a = BotBubbleUser(canvas,message=tmp)
        bubbles.append(a)
        send_message1(tmp)
        print(bubbles)
        
            
    def send_message1(tmp):
        with open("exampledata.json", "r",encoding="utf8") as outfile: 
            jo = json.load(outfile)
        
        for x in jo:
            if bubbles:
                canvas.move(ALL, 0, -10) 
            if x["question"] == tmp.lower():
                b = BotBubbleAgent(canvas,message=x["answer"])
                bubbles1.append(b)
        
        try:
                x = tmp.lower().replace("ngày","").replace("tháng","").replace("năm","").replace(" ","")
                num = 0
                for index in range(len(x)):
                    num += int(x[index])
                        
                print("count: " + str(num))
                tmp1 = str(num)
                num = 0
                for index in range(len(tmp1)):
                        print(tmp1[index])
                        num = num + int(tmp1[index])

                print("count: " + str(num))
                
                
                if num > 9:
                    tmp2 = str(num)
                    num = 0
                    for index in range(len(tmp2)):
                            print(tmp2[index])
                            num = num + int(tmp2[index])

                print("count: " + str(num))

                for x in jo:
                    if bubbles:
                        canvas.move(ALL, 0, -10) 
                    if x["question"] == str(num):
                        b = BotBubbleAgent(canvas,message=x["answer"])
                        bubbles1.append(b)

                
        except:
            print("wrong2")

        try:
                num = 0
                lista = tmp.split("/")
                for item in lista :
                    for index in range(len(item)):
                        print(item[index])
                        num = num + int(item[index])
                        
                print("count: " + str(num))
                tmp1 = str(num)
                num = 0
                for index in range(len(tmp1)):
                        print(tmp1[index])
                        num = num + int(tmp1[index])

                print("count: " + str(num))
                
                
                if num > 9:
                    tmp2 = str(num)
                    num = 0
                    for index in range(len(tmp2)):
                            print(tmp2[index])
                            num = num + int(tmp2[index])

                print("count: " + str(num))

                for x in jo:
                    if bubbles:
                        canvas.move(ALL, 0, -10) 
                    if x["question"] == str(num):
                        b = BotBubbleAgent(canvas,message=x["answer"])
                        bubbles1.append(b)

                
        except:
            print("wrong2")
        

     
    v = StringVar(root, value='')

    entry = Entry(root,width=26, font=("sans-serif", 10),textvariable=v)
    entry.place(x=10, y=550, width=800, height=40)
    # yscrollbar1 = ttk.Scrollbar(entry,orient="vertical",command=canvas.yview)
    # yscrollbar1.pack(side=RIGHT, fill="y")

   

    #buton
    buton = Button(root, width=10, height=2, 
    relief='raised',state='active',command=send_message)
    buton.config(text='SEND', bg='#e4e6eb', font='sans-serif 8 bold')
    buton.place(x=825, y=550)

    buton = Button(root, width=10, height=2, 
    relief='raised',state='active',command=send_message2)
    buton.config(text='RECORD', bg='#e4e6eb', font='sans-serif 8 bold')
    buton.place(x=920, y=550)

    root.mainloop()