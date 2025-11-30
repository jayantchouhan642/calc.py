# calc.py
# Python gui based calculator
import tkinter as tk 
win = tk.Tk()
win.title("Python Calculator")
win.geometry("300x400")

entry = tk.Entry(win, width=18, font=('Arial', 20), borderwidth = 5, relief = "ridge", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            entry.insert(tk.END, f" = {eval(entry.get())}")
        except:
            entry.delete(0,tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)
buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","C","+",
    "="
]
row, col = 1,0 
for b in buttons:
    btn = tk.Button(win, text=b, font=('Arial', 18), height=1, width=4)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col+=1
    if col == 4:
        col = 0
        row += 1
win.mainloop()
