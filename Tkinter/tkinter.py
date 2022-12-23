from tkinter import *
from tkmacosx import Button

root = Tk()
root.title("World Termination Program")
# Window size
root.geometry("500x600")

myLabel3 = Label(root, text = "Enter Your Name: ")
myLabel3.pack(padx = 0, pady = 30)
e = Entry(root, width = 50, borderwidth = 5)
e.pack(padx = 20, pady = 0)
#e.insert()




def myClick():
    # Creating a Label Widget
    myLabel1 = Label(root, text = "Processing...")
    if e.get() != "":
        myLabel2 = Label(root, text = "In charge of " + e.get())

        # Showing it onto the screen
        #myLabel1.grid(row = 0, column = 0)
        myLabel1.pack(padx = 0, pady = 0)   #align center
        myLabel2.pack(padx = 0, pady = 0)
    
    else:
        myLabel2 = Label(root, text = "Error. Please enter your name.")
        myLabel2.pack(padx = 0, pady = 0)


myButton = Button(root,text = "Start", height = 40, width = 100 ,command = myClick, fg = "white", bg = "#DC143C", borderless = 1)
myButton.pack(padx = 0, pady = 60)

root.mainloop()

