# from tkinter import *
# window=Tk()
# l1=Label(window, text="great learning:", bg="blue", fg="red",width=40)
# l1.place(x=5, y=60)
# window.title("welcome to great learning")
# window.minsize(width=200,height=200)
# window.maxsize(width=100,height=500)

# i1=PhotoImage(file="/home/muki/Documents/python full course/chess -AI/black_bishop.png")
# l1 = Label(window, image=i1)



# l1.pack()


# window.mainloop()


# creating button::

# b1=Button(window, text="enter", bg="green", fg ="blue")
# b1.pack()
# window.mainloop()

# entery throught the user

# e1 = Entry(window, width=20, bd = 5,font=("Calibri", 20)) # bd = boder size
# e1.pack()
# window.mainloop()





# from tkinter import *
# window = Tk()
# window.title("welcome to here!")

# window.minsize(width=200,height=400)
# window.maxsize(width=400,height=800)
# l1=Label(window, text="enp name", fg ="blue",bg="red")
# l1.place(x=0,y=10)
# v=StringVar()
# def edtech():
#     x=v.get()
#     print(x)
#     l2.config(text=x,bg="black",fg="yellow")
# e1=Entry(window, font=("corbel", 18),bd=5,textvariable=v)
# e1.place(x=80,y=10)
# b1=Button(window,text="Enter",fg="yellow",bg="Green", command=edtech)
# b1.place(x=120,y=60)
# l2=Label(window,text="nothing", fg="black",bg="brown")
# l2.place(x=120,y=100)
# window.mainloop()



#check button:
# from tkinter import *
# window = Tk()
# window.title("welcome to here!")

# window.minsize(width=200,height=400)
# window.maxsize(width=400,height=800)
# cd=Checkbutton(window, text="Male")
# cd.pack()
# window.mainloop()


#frame::\

from tkinter import *
window = Tk()
window.title("welcome to here!")

window.minsize(width=200,height=400)
window.maxsize(width=400,height=800)
f1=Frame()
f1.pack()
f2 =Frame()
f2.pack()
l1=Label(f1,text="hi sir")
l1.pack()
l2=Label(f2,text="bottom")
l2.pack()
window.mainloop()