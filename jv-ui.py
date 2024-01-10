import os
import time
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import jv

root = tk.Tk()
root.title("JV Process")
root.geometry('900x300')

path = tk.StringVar()
path.set(os.path.abspath("."))
output = tk.StringVar()
output.set("jv_output.csv")

space_row1 = tk.Label(root).grid(row=0, sticky='w')
space_column1 = tk.Label(root).grid(row=1, column=0, sticky='w')
input_label = tk.Label(root, text="Source Folder").grid(row=1, column=1, sticky="w")
input_entry = tk.Entry(root, textvariable=path, state="readonly").grid(row=1, column=2,ipadx=200)

space_row2 = tk.Label(root).grid(row=2, sticky='w')
space_column2 = tk.Label(root).grid(row=3, column=0, sticky='w')
output_label = tk.Label(root, text="Target Filename").grid(row=3, column=1, sticky="w")
output_entry = tk.Entry(root, textvariable=output).grid(row=3, column=2, ipadx=200)

def selectPath():
    path_ = askdirectory()
    if path_ == "":
        path.get()
    else:
        path_ = path_.replace("/", "\\")
        path.set(path_)

def process():
    input_dir = path.get()
    output_file = output.get()
    if output_file == "jv_output.csv":
        output_file = "jv_output_" + str(int(time.time())) + ".csv"
    jv.main(input_dir, output_file)
    messagebox.showinfo("Tips", "Done!")

tk.Button(root, text="Choose", width=10, command=selectPath).grid(row=1, column=3, columnspan=2, sticky="w", padx=10, pady=5)
tk.Button(root, text="Process", width=10, command=process).grid(row=3, column=3, columnspan=2, sticky="w", padx=10, pady=5)

if __name__ == "__main__":
    root.mainloop()