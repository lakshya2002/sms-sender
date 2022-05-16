# API key :  PaSAoThzmwrXOFufLk4s0DUEpJcWVC6I5HjxbGY19QZiged2tN7Bb9tqD5pUd36ksgHw1cGeOYlLrVEJ
import tkinter as tk 
from tkinter import Label, Variable, ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import requests

win = tk.Tk()
win.geometry('500x300')
win.title(' send sms ')
win.wm_iconbitmap('sms.ico')

label_frame = ttk.LabelFrame(win,text="send sms through python")
label_frame.grid(row=1,column=0)

label_1 = ttk.Label(label_frame,text = 'phone number',font=('verdana',10,'bold'))
label_1.grid(row=1,column=0,padx=2.5)

phone_no =tk.IntVar()
phone_num = ttk.Entry(label_frame,width=20,font=('verdana',10,'bold'),textvariable=phone_no)
phone_num.grid(row=1,column=1,padx= 2.5)
phone_num.insert('end','phone number')

label_2 = ttk.Label(label_frame,text = 'Enter message',font=('verdana',10,'bold'))
label_2.grid(row=2,column=0,padx=2.5,pady=2.5)

message = tk.Text(label_frame,height=5,width=20,font=('verdana',10,'bold'))
message.grid(row=2,column=1,padx=4.5,pady=5)
message.insert('end','Message')

def send_sms():
    number = phone_no.get()
    messages = message.get(1.0,'end')
    url = "https://www.fast2sms.com/dev/bulk"
    api = "PaSAoThzmwrXOFufLk4s0DUEpJcWVC6I5HjxbGY19QZiged2tN7Bb9tqD5pUd36ksgHw1cGeOYlLrVEJ"
    querystring  ={
        "authorization":api,
        "sender_id":"FSTSMS",
        "message":messages,
        "language":"english",
        "route":"p",
        "numbers":number
    }
    headers = {
        "cache-control":"no-cache"
    }
    requests.request("GET",url,headers=headers,params=querystring)
    messagebox.showinfo("SMS Sent","Sent Successfully")


send  =ttk.Button(label_frame,text='SEND',cursor='hand2',command=send_sms)
send.grid(row=3,columnspan=4,pady=5)


win.mainloop()

