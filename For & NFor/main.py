import tkinter as tk
from home import HomeWindow

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Window")
        self.master.geometry("1500x1000")
        self.master.configure(bg="light blue")

        self.for_button = tk.Button(self.master, text="For Loop", command=self.open_for_loop, bg = "orange")
        self.for_button.pack(pady=10)

        self.nested_button = tk.Button(self.master, text="Nested For Loop", command=self.open_nested_loop, bg = "orange")
        self.nested_button.pack(pady=10)

    def open_for_loop(self):
        self.for_window = tk.Toplevel(self.master)
        self.for_window.configure(bg="light green")
        self.for_window.geometry("1500x1000")
        self.for_loop = HomeWindow(self.for_window, loop_type="for")

    def open_nested_loop(self):
        self.nested_window = tk.Toplevel(self.master)
        self.nested_window.configure(bg="light green")
        self.nested_window.geometry("1500x1000")
        self.nested_loop = HomeWindow(self.nested_window, loop_type="nested")


def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()

