import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    win.title(f"Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor Application - {filepath}")

win = tk.Tk()
win.title("Text Editor")
win.rowconfigure(0, minsize=900, weight=1)
win.columnconfigure(1, minsize=900, weight=1)

txt_edit = tk.Text(win)
fr_buttons = tk.Frame(win, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open File", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save File", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
btn_save.grid(row=1, column=0, sticky="ew", padx=10)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

win.mainloop()

