import tkinter as tk
from tkinter import ttk
import time

class HomeWindow:
    def __init__(self, master, loop_type):
        self.master = master
        self.loop_type = loop_type
        self.table_rows = []

        if self.loop_type == "for":
            self.master.title("For Loop Window")
        elif self.loop_type == "nested":
            self.master.title("Nested For Loop Window")

        self.label1 = tk.Label(master, text="Enter the first loop value:", bg = "light blue")
        self.label1.pack(pady=10)

        self.loop_value_entry = tk.Entry(master)
        self.loop_value_entry.pack(pady=10)

        if self.loop_type == "nested":
            self.label2 = tk.Label(master, text="Enter the second loop value:", bg = "light blue")
            self.label2.pack(pady=10)

            self.second_loop_value_entry = tk.Entry(master)
            self.second_loop_value_entry.pack(pady=10)

        self.run_button = tk.Button(master, text="Run Loop", command=self.run_loop, bg = "yellow")
        self.run_button.pack(pady=10)

        self.table = ttk.Treeview(master)
        self.table["columns"] = ("Initialization", "Condition", "Increment/Decrement")
        self.table.heading("Initialization", text="Initialization")
        self.table.heading("Condition", text="Condition")
        self.table.heading("Increment/Decrement", text="Increment/Decrement")
        self.table.pack(pady=10)

    def run_loop(self):
        self.clear_table()
        try:
            loop_value = int(self.loop_value_entry.get())
            if self.loop_type == "nested":
                second_loop_value = int(self.second_loop_value_entry.get())
                self.display_nested_loop(loop_value, second_loop_value)
            else:
                self.display_for_loop(loop_value)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid integer values.")

    def clear_table(self):
        for row in self.table_rows:
            self.table.delete(row)
        self.table_rows = []

    def display_for_loop(self, loop_value):
        for i in range(1, loop_value + 1):
            print(i)
            time.sleep(0.5)
            print('i+=1=>')
            time.sleep(0.5)
            self.table_rows.append(self.table.insert("", "end", values=(f"i = {i}", f"i <= {loop_value}", "i++")))
            

    def display_nested_loop(self, loop_value, second_loop_value):
        for i in range(1, loop_value + 1):
            print(i)
            time.sleep(0.5)
            print('i+=1=>')
            time.sleep(0.5)
            for j in range(1, second_loop_value + 1):
                print(j)
                time.sleep(0.5)
                print('j+=1=>')
                time.sleep(0.5)
            
                self.table_rows.append(self.table.insert("", "end", values=(f"i = {i}, j = {j}", f"i <= {loop_value} && j <= {second_loop_value}", "j++")))


def main():
    root = tk.Tk()
    app = HomeWindow(root, loop_type="for")
    root.mainloop()


if __name__ == "__main__":
    main()

