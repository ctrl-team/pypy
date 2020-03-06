import serial
import time
from tkinter import *

print(int(16/32))
def sendToArduino(fstRow, scdRow):
    space = ' '

    firstRowAdd = 16 - len(fstRow)
    fstRow = fstRow + (firstRowAdd * space)

    secondRowAdd = 16 - len(scdRow)
    scdRow = scdRow + (secondRowAdd * space)

    if(len(fstRow) + len(scdRow) <= 32):
        for i in range(30):
            for i in range(len(fstRow)):
                arduino.write(fstRow[i].encode())
            for i in range(len(scdRow)):
                arduino.write(scdRow[i].encode())

            time.sleep(0.2)
    else:
        print("data must be <= 32")

arduino = serial.Serial('COM4', 9600)

root = Tk()
root.geometry("230x70")

Label(root, text="1st Row").grid(row=0, sticky=W)
Label(root, text="2nd Row").grid(row=1, sticky=W)

e1 = Entry(root)
e2 = Entry(root)

entry1data = e1.get()
entry2data = e2.get()

btn1 = Button(root, text="Enter", command= lambda: sendToArduino(e1.get(), e2.get()))

e1.grid(row=0, column=1, padx=5, pady=5)
e2.grid(row=1, column=1, padx=5, pady=5)
btn1.grid(row=0, column=2, padx=5, pady=5)

root.mainloop()

