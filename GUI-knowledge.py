from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() #หน้าจอหลักโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x400') #ขนาดโปรแกรม

#B1 = ttk.Button(GUI,text='เงินมีกี่บาท')
#B1.pack(ipadx=20,ipady=20)

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30 , y=30)

#######
def Button2():
    text = '300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)


FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=300)
B2 = ttk.Button(FB1,text='เงินมีกี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)
########
def Button3():
    text = 'Python 101, Math'
    messagebox.showinfo('วิชาเรียนวันที่ 10-20 ก.พ.',text)


FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=100,y=300)
B3 = ttk.Button(FB1,text='สัปดาห์เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20)
########

GUI.mainloop()
