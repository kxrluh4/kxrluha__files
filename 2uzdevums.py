import tkinter as tk
from tkinter import messagebox
logs=tk.Tk()
logs.geometry("400x350")
logs.title("dalisanas kalkulators")

def dali():
    try: 
        teksts1=teksts_2.get()
        teksts2=teksts_4.get()

        skaitlis1=int(teksts1)
        skaitlis2=int(teksts2)
        dalijums=skaitlis1/skaitlis2
        label_rezultats.config(text=f"dali: {dalijums}")
    except ValueError:
        messagebox.showerror("bridinajums", "Ievadiet derīgus skaitļus")
    except ZeroDivisionError:
        messagebox.showerror("Kļūda", "Dalītājs nedrīkst būt nulle")

teksts_1=tk.Label(logs, text="pirmais skaitlis:",)

teksts_2=tk.Entry(logs)


teksts_3=tk.Label(logs, text="otrais skaitlis:",)

teksts_4=tk.Entry(logs)

poga1=tk.Button(logs,text="dali", command=dali)
label_rezultats=tk.Label(logs, text="dalijums: ")


teksts_1.pack()
teksts_2.pack()
teksts_3.pack()

teksts_4.pack()
poga1.pack(pady=10)
label_rezultats.pack()  


logs.mainloop()







