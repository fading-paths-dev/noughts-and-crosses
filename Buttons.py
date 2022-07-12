from tkinter import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton()
        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        textButton = Button(self, text="Text", command=self.displayText)

        # place button at (0,0)
        exitButton.place(x=0, y=0)
        textButton.place(x=0, y=50)

    def clickExitButton(self):
        exit()

    def displayText(self):
        print("test")


root = Tk()
app = Window(root)
root.wm_title("Tkinter button")
root.geometry("320x200")
root.mainloop()
