import tkinter
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import HashSnake
from algorithms.algorithms import md5, sha256, sha512
import threading

class EnvironmentMain(object):
    frame = None
    heading_text = None
    middle_text = None
    start_button = None
    exit_button = None

class EnvironmentInner(object):
    label_1 = None
    entry_1 = None
    chvar = None
    label_2 = None
    label_3 = None
    entry_2 = None
    rad = None
    rad1 = None
    rad2 = None
    button = None
    button2 = None

def function_threaded(function):

    def wrapper(*args, **kwargs):
        threading.Thread(target = function, args = args, kwargs = kwargs).start()

class GUIApp():
    
    
    
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("HashSnake")
        self.root.geometry("1024x620+430+250")
        self.environment: EnvironmentMain = EnvironmentMain()
        self.environment_c: EnvironmentInner = EnvironmentInner()
        
    def __repr__(self):
        return f"<GUIApp>"

    def destroy_all(self):
        if self.environment_c.label_1:
            self.environment_c.label_1.destroy()
        if self.environment_c.entry_1:
            self.environment_c.entry_1.destroy()
        if self.environment_c.entry_2:
            self.environment_c.entry_2.destroy()
        if self.environment_c.rad:
            self.environment_c.rad.destroy()
        if self.environment_c.rad1:
            self.environment_c.rad1.destroy()
        if self.environment_c.rad2:
            self.environment_c.rad2.destroy()
        if self.environment_c.button:
            self.environment_c.button.destroy()
        if self.environment_c.button2:
            self.environment_c.button2.destroy()
        if self.environment_c.label_2:
            self.environment_c.label_2.destroy()
        if self.environment_c.label_3:
            self.environment_c.label_3.destroy()

    def start(self):
        self.destroy_all()

        self.environment.heading_text = ttk.Label(self.root, text = "HashSnake", font = ("Verdana 16"), compound = "center")
        self.environment.heading_text.pack()
        self.environment.middle_text = tkinter.Label(self.root,
        text = "The creator of this program is not responsible for any misuse or damage caused by it.", compound = "center", fg = "red",
        bg = "yellow")
        self.environment.middle_text.pack(pady = 25)
        self.environment.start_button = ttk.Button(self.root, text = "start", compound = "center", width = 25, command = self.start_hashsnake)
        self.environment.start_button.pack(pady = 25)
        self.environment.exit_button = ttk.Button(self.root, text = "exit", compound = "center", width = 25, command = exit)
        self.environment.exit_button.pack(pady = 25)
        self.root.mainloop()

    def start_hashsnake(self):
        self.destroy_all()
        self.environment.start_button.destroy()
        self.environment.exit_button.destroy()
        self.environment.middle_text.destroy()
        self.environment.heading_text.destroy()
        self.environment_c.label_1 = tkinter.Label(self.root, text = "Enter hash: ", font = "Verdana 12")
        self.environment_c.label_1.place(x = 60, y = 60)
        self.environment_c.entry_1 = tkinter.Entry(self.root, font = "Verdana 12")
        self.environment_c.entry_1.insert(0, "<hash>")
        self.environment_c.entry_1.place(x = 60, y = 90)
        self.environment_c.label_3 = tkinter.Label(self.root, text="Enter wordlist: ", font="Verdana 12")
        self.environment_c.label_3.place(x=60, y=120)
        self.environment_c.entry_2 = ttk.Entry(self.root, font="Verdana 12")
        self.environment_c.entry_2.insert(0, "Path of the wordlist")
        self.environment_c.entry_2.place(x=55, y = 140)
        self.environment_c.chvar = tkinter.IntVar()
        self.environment_c.chvar.set(0)
        self.environment_c.rad = ttk.Radiobutton(self.root, text = "SHA256", variable = self.environment_c.chvar, value = 1)
        self.environment_c.rad.place(x = 120, y = 180)
        self.environment_c.rad1 = ttk.Radiobutton(self.root, text = "MD5", variable = self.environment_c.chvar, value = 2)
        self.environment_c.rad1.place(x = 120, y = 200)
        self.environment_c.rad2 = ttk.Radiobutton(self.root, text = "SHA512", variable = self.environment_c.chvar, value = 3)
        self.environment_c.rad2.place(x = 120, y = 220)
        self.environment_c.button = ttk.Button(self.root, text = "Start cracking", command = self.start_cracking)
        self.environment_c.button.place(x = 120, y = 280)
        self.environment_c.button2 = ttk.Button(self.root, text="Back", command=self.start)
        self.environment_c.button2.place(x=120, y=300)

    def start_cracking(self):
        hash_value, algorithm, wordlist = self.environment_c.entry_1.get(), self.environment_c.chvar.get(), self.environment_c.entry_2.get()
        algorithms = {1: sha256(), 2: md5(), 3: sha512()}
        if algorithm not in algorithms:
            messagebox.showerror("Error", "Algorithm must be one of the following: SHA256, MD5, SHA512")
            self.start_hashsnake()
        self.environment_c.label_2 = ttk.Label(self.root, text = "Cracking...", font = "Verdana 12")
        self.environment_c.label_2.place(x = 500, y = 60)
        try:
            _object = HashSnake.HashSnake(hash_value.split(","), algorithms[algorithm], wordlist, False, False)
            results = _object.start()
            if not results:
                self.environment_c.label_2 = ttk.Label(self.root, text = "No results", font = "Verdana 12")
                self.environment_c.label_2.place(x = 500, y = 60)
            else:
                self.environment_c.label_2.destroy()
                messagebox.showinfo("HashSnake", f"Recovered: {len(results)}")
                self.environment_c.label_2 = ttk.Label(self.root, text = f"Results: {",".join(f"{_} = {plain_text}" for plain_text, _ in results)}",
                font = "Verdana 12", wraplength = 450)
                self.environment_c.label_2.place(x = 500, y = 60)
        except Exception as exception:
            messagebox.showerror("Error", f"Hash Snake could not be started.\nError: {exception}")
            self.destroy_all()
            self.start_hashsnake()

if __name__ == "__main__":
    GUIApp().start()