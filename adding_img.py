from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk,Image
window = Tk()
window.title("images!!!")
window.resizable(0, 0)
window.iconbitmap('image/mario.ico')                                         #adding icon in title
# create frame
frame=Frame(window, width=600, height=500, bg='sky blue', relief=GROOVE, bd=2)
frame.pack(padx=10, pady=10)
# create thumbanials of all images  
i1 = Image.open('image/msn.png')
i1.thumbnail((550, 450))
i2 = Image.open('image/mns.png')
i2.thumbnail((550, 450))
i3 = Image.open('image/ney.png')
i3.thumbnail((550, 450))
i4 = Image.open('image/primeney.png')
i4.thumbnail((550, 450))
i5 = Image.open('image/ragn.png')
i5.thumbnail((550, 450))
i6 = Image.open('image/thor.png')
i6.thumbnail((550, 450))
i7 = Image.open('image/loki.png')
i7.thumbnail((550, 450))
i8 = Image.open('image/tobey.png')
i8.thumbnail((550, 450))

# open images to use with labels
img1 = ImageTk.PhotoImage(i1)
img2 = ImageTk.PhotoImage(i2)
img3 = ImageTk.PhotoImage(i3)
img4 = ImageTk.PhotoImage(i4)
img5 = ImageTk.PhotoImage(i5)
img6 = ImageTk.PhotoImage(i6)
img7 = ImageTk.PhotoImage(i7)
img8 = ImageTk.PhotoImage(i8)
# create list of images
images = [img1, img2,img3, img4, img5,img6,img7,img8]
# configure the image to the Label in frame
i = 0
image_label = Label(frame, image=images[i])
image_label.pack()
# create functions to display previous and next images
# create functions to display previous and next images
def previous():
    global i
    i = i - 1
    try:
        image_label.config(image=images[i])
    except:
        i = 0
previous()
def another():
    global i
    i = i + 1
    try:
        image_label.config(image=images[i])
    except:
        i = 0
another()

# create buttons    
btn1 = Button(window, text="Prev",width=8, bd=5 ,bg='sky blue', fg='black', font=('cosmic sans serif ',12,BOLD), relief=RAISED,command=previous)
btn1.pack(side=LEFT, padx=60, pady=5)

btn3 = Button(window, text="Exit", width=8,bd=5, bg='sky blue', fg='black', font=('cosmic sans serif ',12,BOLD), relief=RAISED, command=window.destroy)
btn3.pack(side=LEFT, padx=60, pady=5)
btn2 = Button(window, text="Next", width=8, bd=5,bg='sky blue', fg='black', font=('cosmic sans serif ',12,BOLD), relief=RAISED, command=another)
btn2.pack(side=LEFT, padx=60, pady=5)

window.mainloop()