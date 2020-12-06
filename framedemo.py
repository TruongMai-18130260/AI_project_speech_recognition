from tkinter import * 
from tkinter import messagebox 
import a as apy
  
root = Tk() 

root.geometry("400x300")  

 


btn1 = Button(root,text="Use Agent",padx=15,pady=25,bg='#FF5733',width=50,command=apy.printa)
btn1.pack(padx=50,pady=50)

btn2 = Button(root,text="Train Agent",padx=15,pady=25,bg='#FF5733',width=50,command=apy.printa)
btn2.pack(padx=50,pady=0)
  
root.mainloop()  