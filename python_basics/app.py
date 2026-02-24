from tkinter import *
def Login():
    print(f"Login From Here")


root = Tk()
root.geometry("600x600")
frame_one =Frame(root)
frame_one.pack()

Button_one = Button(frame_one,text= "Login From Here Sir",command= "Login")
Button_one.pack()

root.mainloop()

