# this is Receiver file or client side 
import os
import socket
import time
from tkinter import *


def connect():

    host = txtfld.get()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Trying to connect to socket.
    try:
        sock.connect((host, 22222))
        print("Connected Successfully")
    except:
        print("Can't Connect to Server :/ ")
        exit(0)

    # rece file details from the sender - server - side
    file_name = sock.recv(100).decode()
    file_size = sock.recv(100).decode()

    # Opening and reading file.
    with open("./File Rec/" + file_name, "wb") as file:
        c = 0
        # Starting the time capture.
        start_time = time.time()

        # Running the loop while file is recieved.
        while c <= int(file_size):
            data = sock.recv(1024)
            if not (data):
                break
            file.write(data)
            c += len(data)

        # Ending the time capture.
        end_time = time.time()

    msg = "File transfer Complete! "
    print(msg , "Total time: ", end_time - start_time)
    lbl.config(text=msg)
    # Closing the socket.
    sock.close()

"""
GUI Setting up
and put widget on the screen
and assign the connect button function
"""

window = Tk()
window.title("File Receiver")
window.geometry("400x400")

hlbl=Label(window, text="Enter The Host wanna to connect", fg='red', font=("Helvetica", 12))
hlbl.place(x=40, y=20)

txtfld=Entry(window, text="", bd=5)
txtfld.place(x=30, y=60)

btn=Button(window, text="Connect", fg='blue' , command=connect)
btn.place(x=300, y=100)

lbl=Label(window, text="", fg='red', font=("Helvetica", 12))
lbl.place(x=40, y=140)


window.mainloop()
