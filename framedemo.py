from tkinter import * 
from tkinter import messagebox 
import a as apy
import tom as tomAgent
  
root = Tk() 

root.geometry("400x300")  

root.title("TỬ VI CHATBOT")

btn1 = Button(root,text="Xem tử vi",padx=15,pady=25,bg='#b42025',fg="white",width=50,command=tomAgent.initFrame)
btn1.pack(padx=50,pady=50)

btn2 = Button(root,text="Luyện phần mềm",padx=15,pady=25,bg='#b42025',fg="white",width=50,command=apy.printa)
btn2.pack(padx=50,pady=0)
  
root.mainloop()  