from tkinter import *
import math

def leftClickButton(event):
    bmi = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    print(bmi)
    labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    if  bmi > 30:
        labelTextResult.configure(text="อ้วนมาก")
        print('อ้วนมาก bmi > 30')
    elif bmi >= 25:
        labelTextResult.configure(text="อ้วน")
        print('อ้วน bmi >= 25')
    elif bmi >= 23:
        labelTextResult.configure(text="น้ำหนักเกิน")
        print('น้ำหนักเกิน bmi >= 23')
    elif bmi >= 18.6:
        labelTextResult.configure(text="น้ำหนักปกติ เหมาะสม")
        print('น้ำหนักปกติ เหมาะสม bmi >= 18')
    else:
        labelTextResult.configure(text="ผอมเกินไป")
        print('ผอมเกินไป bmi < 18.5 ')

main = Tk()
labelHeight = Label(main,text = "ส่วนสูง (CM.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(main)
textBoxHeight.grid(row=0, column=1)
labelWeight = Label(main,text = "น้ำหนัก (Kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(main)
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(main, text = "คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2, column=0)
labelResult = Label(main,text = "ผลลัพธ์")
labelResult.grid(row=2, column=1)
labelTextResult = Label(main,text = "ความหมาย")
labelTextResult.grid(row=3, column=1)
main.mainloop()