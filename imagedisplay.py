from tkinter import *

window = Tk()
window.title("My Image")
window = Canvas(window, width = 450, height = 450)
window.pack()
myimage = PhotoImage(file = "images/cat.png")
window.create_image(0,0,anchor = NW, image = myimage)
window.mainloop()
 