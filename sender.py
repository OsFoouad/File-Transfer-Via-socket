# Sender or Server File 

import os
import socket
import time
from tkinter import *
        
    # Creating a socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 22222))
sock.listen(5)
print("Host Name: ", sock.getsockname())
client, addr = sock.accept()

def sendfile():
    # Getting file details.
    file_name = txtfld.get()
    file_size = os.path.getsize(file_name)

    # Sending file_name and detail.
    client.send(file_name.encode())
    client.send(str(file_size).encode())

    # Opening file and sending data.
    with open(file_name, "rb") as file:
        c = 0
        # Starting the time capture.
        start_time = time.time()

        # Running loop while c != file_size.
        while c <= file_size:
            data = file.read(1024)
            if not (data):
                break
            client.sendall(data)
            c += len(data)

        # Ending the time capture.
        end_time = time.time()

    msg = "File transfer Complete! "
    print(msg , "Total time: ", end_time - start_time)
    lbl.config(text=msg)
    # Cloasing the socket.
    sock.close()

###################

"""
GUI Setting up
and put widget on the screen
and assign the connect button function
"""

window = Tk()
window.title("File Sender")
window.geometry("400x400")

helplbl=Label(window, text="Client connected & wanna receive", fg='red', font=("Helvetica", 12))
helplbl.place(x=40, y=20)

hostlbl=Label(window, text="if ok enter file name with extension", fg='red', font=("Helvetica", 12))
hostlbl.place(x=40, y=60)

txtfld=Entry(window, text="Enter the file name", bd=5)
txtfld.place(x=40, y=100)

btn=Button(window, text="Send File", fg='blue' , command=sendfile)
btn.place(x=100, y=140)


lbl=Label(window, text="", fg='red', font=("Helvetica", 12))
lbl.place(x=40, y=200)


window.mainloop()
