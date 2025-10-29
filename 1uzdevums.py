from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox
Logs=tk.Tk()
Logs.geometry("400x350")
Logs.title("kalkulators")
def saskaitit():
    try: 
        teksts1=teksts_2.get()
        teksts2=teksts_4.get()

        skaitlis1=int(teksts1)
        skaitlis2=int(teksts2)
        summa=skaitlis1+skaitlis2
        label_rezultats.config(text=f"summa: {summa}")
    except:
        messagebox.showerror("Kļūda", "Ievadiet derīgus skaitļus")


teksts_1=tk.Label(Logs, text="pirmais skaitlis:",)

teksts_2=tk.Entry(Logs)


teksts_3=tk.Label(Logs, text="otrais skaitlis:",)

teksts_4=tk.Entry(Logs)

poga1=tk.Button(Logs,text="saskaitit", command=saskaitit)
label_rezultats=tk.Label(Logs, text="summa: ")


teksts_1.pack()
teksts_2.pack()
teksts_3.pack()

teksts_4.pack()
poga1.pack(pady=10)
label_rezultats.pack()  




Logs.mainloop()