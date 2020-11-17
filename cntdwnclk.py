#! /usr/bin/env python3

from tkinter import *
import time
from playsound import playsound

root = Tk()
root.geometry('400x300')
root.resizable(1,1)
root.config(bg ='gray7')
root.title('Countdown Clock and Timer')
Label(root, text = 'Countdown Timer', font = 'arial 20 bold',
    bg = 'gray7', fg='lime green').pack()
    

Label(root, font = 'arial 15 bold', text = 'Current Time :', 
    bg = 'gray21', fg = 'lime green').place(x = 60, y = 60)

    
def clock():
    clock_time = time.strftime('%I:%M:%S: %p')
    curr_time.config(text = clock_time)
    curr_time.after(1000,clock)
    
curr_time = Label(root, font ='arial 15 bold', text = '', fg = 'lime green', 
    bg = 'gray21')
curr_time.place(x = 210, y = 60)
clock()

sec = StringVar()
Entry(root, textvariable = sec, width = 2, font = 'arial 14').place(x=260, y=120)
sec.set('00')

mins = StringVar()
Entry(root, textvariable = mins, width =2, font = 'arial 14').place(x=235, y=120)
mins.set('00')

hrs = StringVar()
Entry(root, textvariable = hrs, width =2, font = 'arial 14').place(x=210, y=120)
hrs.set('00')


def countdown():
    times = int(hrs.get())*3600 + int(mins.get())*60 + int(sec.get())
    while times > -1:
        minute,second = (times // 60, times % 60)
        
        hour = 0
        if minute >60:
            hour, minute = (minute // 60, minute % 60)
        
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
        
        root.update()
        time.sleep(1)
        
        if(times == 0):
            playsound('alarm.mp3')
            sec.set('00')
            mins.set('00')
            hrs.set('00')
        times -= 1
        
def close():
    root.destroy()
        
Label(root, font = 'arial 15 bold', text = 'Set the Time', 
    bg = 'gray21', fg = 'lime green').place(x = 60, y = 120)
    
Button(root, text='START', bd = '5', command = countdown, bg = 'gray21', 
    fg = 'lime green', font = 'arial 10 bold').place(x=150, y=180)
    
Button(root, text='EXIT', bd = '5', command = close , bg = 'gray21', 
    fg = 'lime green', font = 'arial 10 bold').place(x=156, y=240)
    
root.mainloop()

