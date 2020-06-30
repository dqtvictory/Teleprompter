import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import socket
from time import sleep
from _thread import start_new_thread

SERVER_IP = "127.0.0.1"
PORT = 11000

def worker():
    # get the Text box object from the global scope to be able to extract text from it
    global textbox
    last_text = ""
    while True:
        sleep(0.2)
        # kinda weird method in tkinter to get the text from beginning to the end of textbox
        text = textbox.get('1.0', 'end')
        if last_text != text:
            last_text = text
            data = text + "$"
            conn.sendall(data.encode())
    

if __name__ == "__main__":
    # start the server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, PORT))
    server.listen()

    # accept the connection
    conn, addr = server.accept()
    print(f"{addr} connected!")

    # initialize the UI
    app = tk.Tk()
    app.minsize(600,600)
    app.title("Server")
    textbox = ScrolledText(app, wrap=tk.WORD, font=("Arial", 24))
    textbox.pack()

    # start the worker's thread
    start_new_thread(worker, ())

    app.mainloop()

    # this program is so simple that I won't bother closing the socket and ending the thread (thou I really should)