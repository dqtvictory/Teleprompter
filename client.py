import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import socket
from time import sleep
from _thread import start_new_thread

SERVER_IP = "127.0.0.1"
PORT = 11000
BUFFER = 4096

def listen():
    # get the Text box object from the global scope to maintain and update it
    global textbox

    # listen to server
    while True:
        received_all = False
        text = ""

        # make sure we receive all of the message
        while not received_all:
            data = client.recv(BUFFER).decode()
            i = data.find("$")
            if i == -1:
                text += data
            else:
                text += data[:i]
                received_all = True

        # what a weird way in tkinter to clear the textbox and update it with new text (I have never done anything with tkinter before)
        textbox.delete('1.0', 'end')
        textbox.insert(tk.INSERT, text)
    

if __name__ == "__main__":
    # connect to the server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, PORT))
    
    # initialize the UI
    app = tk.Tk()
    app.minsize(600,600)
    app.title("Client")
    textbox = ScrolledText(app, wrap=tk.WORD, font=("Arial", 24))
    textbox.pack()

    # start the listener's thread
    start_new_thread(listen, ())

    app.mainloop()
    # this program is so simple that I won't bother closing the socket and ending the thread (thou I really should)