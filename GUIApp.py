import tkinter
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import HashSnake
from algorithms.algorithms import md5, sha256, sha512, sha1, sha224
import threading
import queue

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
    label_4 = None
    label_5 = None
    entry_2 = None
    entry_3 = None
    rad = None
    rad1 = None
    rad2 = None
    rad3 = None
    rad4 = None
    button = None
    button2 = None
    panedwindow = None

def function_threaded(function):

    def wrapper(*args, **kwargs):
        threading.Thread(target = function, args = args, kwargs = kwargs).start()

class GUIApp():



    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("HashSnake")
        self.root.geometry("1024x620+430+250")
        self.root.configure(bg="#111111")
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.resizable(False, False)
        self.style = ttk.Style()
        self.style.configure("Dark.TLabel", font = ("Verdana", 13), background = "#111111", foreground = "#cccccc")
        self.style.configure("Dark.TEntry",
        font = ("Verdana", 13), background = "#1c1c1c", foreground = "green")
        self.style.configure("Dark.TRadiobutton",
        background = "#111111", foreground = "green", borderwidth = 0, font = ("Verdana", 11))
        self.results = None
        self.running: bool = False
        self.queue = queue.Queue()
        self.environment: EnvironmentMain = EnvironmentMain()
        self.environment_c: EnvironmentInner = EnvironmentInner()

    def __repr__(self):
        return f"<GUIApp>"

    def destroy_all(self):
        for variables in vars(self.environment_c).values():
            if variables:
                try:
                    variables.destroy()
                except:
                    pass

    def start(self):
        self.destroy_all()
        style = ttk.Style()
        style.map("TButton", background = [("active", "#00aa66")])
        self.environment.heading_text = ttk.Label(self.root, text = "HashSnake", font = "Verdana 32", compound = "center", style = "Dark.TLabel")
        self.environment.heading_text.pack()
        self.environment.middle_text = tkinter.Label(self.root,
                text="The creator of this program is not responsible for any misuse or damage caused by it.",
                compound="center", fg="#ff5555",
                bg="#111111", font="Verdana 12", wraplength=700,
                justify="center")
        self.environment.middle_text.pack(pady=25)
        self.environment.start_button = tkinter.Button(self.root, text = "Start Hash Cracking", compound = "center", width = 50, command = self.start_hashsnake,
        activebackground = "#111111", activeforeground = "green", bg = "#111111", fg = "green", borderwidth = 0)
        self.environment.start_button.pack(pady = 5)
        self.environment.exit_button = tkinter.Button(self.root, text = "Exit", compound = "center", width = 50, command = self.exit,
        activebackground = "#111111", activeforeground = "green",bg = "#111111", fg = "green", borderwidth = 0)
        self.environment.exit_button.pack(pady = 25)
        self.root.mainloop()


    def start_hashsnake(self):
        self.destroy_all()
        self.environment.start_button.destroy()
        self.environment.exit_button.destroy()
        self.environment.middle_text.destroy()
        self.environment.heading_text.destroy()
        self.environment_c.label_1 = ttk.Label(self.root, text = "Enter hash: ", font = "Verdana 12", style = "Dark.TLabel")
        self.environment_c.label_1.place(x = 320, y = 60)
        self.environment_c.entry_1 = ttk.Entry(self.root, style="Dark.TEntry")
        self.environment_c.entry_1.place(x=320, y=90)
        self.environment_c.label_5 = ttk.Label(self.root, text = "Enter salt: ", font = "Verdana 12", style = "Dark.TLabel")
        self.environment_c.label_5.place(x = 480, y = 60)
        self.environment_c.entry_3 = ttk.Entry(self.root, style = "Dark.TEntry")
        self.environment_c.entry_3.place(x = 480, y = 90)
        self.environment_c.label_3 = ttk.Label(self.root, text="Enter wordlist: ", font="Verdana 12", style = "Dark.TLabel")
        self.environment_c.label_3.place(x = 320, y=120)
        self.environment_c.entry_2 = ttk.Entry(self.root, font="Verdana 12", style = "Dark.TEntry")
        self.environment_c.entry_2.place(x=320, y = 150)
        self.environment_c.chvar = tkinter.IntVar()
        self.environment_c.chvar.set(0)
        self.environment_c.rad = ttk.Radiobutton(self.root, text = "SHA256", variable = self.environment_c.chvar, value = 1, style = "Dark.TRadiobutton")
        self.environment_c.rad.place(x = 320, y = 200)
        self.environment_c.rad1 = ttk.Radiobutton(self.root, text = "MD5", variable = self.environment_c.chvar, value = 2, style = "Dark.TRadiobutton")
        self.environment_c.rad1.place(x = 320, y = 220)
        self.environment_c.rad2 = ttk.Radiobutton(self.root, text = "SHA512", variable = self.environment_c.chvar, value = 3, style = "Dark.TRadiobutton")
        self.environment_c.rad2.place(x = 320, y = 240)
        self.environment_c.rad3 = ttk.Radiobutton(self.root, text = "SHA1", variable = self.environment_c.chvar, value = 4, style = "Dark.TRadiobutton")
        self.environment_c.rad3.place(x = 480, y = 200)
        self.environment_c.rad4 = ttk.Radiobutton(self.root, text = "SHA224", variable = self.environment_c.chvar, value = 5, style = "Dark.TRadiobutton")
        self.environment_c.rad4.place(x = 480, y = 220)
        self.environment_c.button = tkinter.Button(self.root, text = "Start cracking", command = self.start_cracking,
        activebackground = "#111111", activeforeground = "green", bg="#111111", fg = "green", borderwidth = 0, width = 50)
        self.environment_c.button.place(x = 320, y = 280)
        self.environment_c.button2 = tkinter.Button(self.root, text="Back", command=self.start,
        activebackground = "#111111", activeforeground = "green", bg = "#111111", fg = "green", borderwidth = 0, width = 50)
        self.environment_c.button2.place(x=320, y=330)

    def start_cracking(self):
        if self.environment_c.label_2:
            self.environment_c.label_2.destroy()
        if self.environment_c.label_4:
            self.environment_c.label_4.destroy()
        hash_value, algorithm, wordlist, salt = self.environment_c.entry_1.get(), self.environment_c.chvar.get(), self.environment_c.entry_2.get(), self.environment_c.entry_3.get()
        self.environment_c.entry_3.get()
        algorithms = {1: sha256(), 2: md5(), 3: sha512(), 4: sha1(), 5: sha224()}
        if algorithm not in algorithms:
            messagebox.showerror("Error", "Algorithm must be one of the following: SHA256, MD5, SHA512")
            self.start_hashsnake()
        try:
            _object = HashSnake.HashSnake(hash_value.split(","), algorithms[algorithm], wordlist, False, False)
            self.results = _object.start(salt)
            if not self.results:
                messagebox.showinfo("HashSnake", f"No recovered hashes.")
                self.environment_c.label_2 = ttk.Label(self.root, text = "No results", font = "Verdana 12")
                self.environment_c.label_2.place(x = 330, y = 380)
            else:
                if self.environment_c.label_2:
                    self.environment_c.label_2.destroy()
                messagebox.showinfo("HashSnake", f"Recovered: {len(self.results)}")
                self.environment_c.label_2 = ttk.Label(self.environment_c.panedwindow, text = f"Results: {",".join(f"{_} = {plain_text}" for plain_text, _ in self.results)}",
                font = "Verdana 12", wraplength = 450, background = "#111111", foreground = "green")
                self.environment_c.label_2.place(x = 330, y = 380)
                self.environment_c.label_4 = ttk.Label(self.root, text = f"Results are saved in 'plain.txt'.", font = "Verdana 12", wraplength = 450, background = "black", foreground = "green")
                self.environment_c.label_4.place(x = 330, y = 500)
        except Exception as exception:
            messagebox.showerror("Error", f"Hash Snake could not be started.\nError: {exception}")
            self.destroy_all()
            self.start_hashsnake()

    def exit(self):
        answer = messagebox.askyesno("Warning", message = "Are you sure you want to exit?", icon = "question")
        if answer:
            self.root.destroy()
