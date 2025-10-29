import tkinter as tk
from tkinter import messagebox
logs=tk.Tk()
logs.geometry("600x550")
logs.title("spiediena aprekins")
logs.background="#AC97CC"
#izveidoju logu spiediena aprekins

def aprekinat_spiedienu():# aprēķina spiedienu pēc formulas p=F/S
    try:
        teksts1=ievade_speks.get()
        teksts2=ievade_laukums.get()

        F=speks=int(teksts1)
        S=laukums=int(teksts2)
        p=spiediens=F/S
        rezultats.config(text=f"spiediens ir: {p} Pa")
        if S==0:
            messagebox.showerror("Laukums nedrīkst būt nulle")
        else:
            p=F/S
            rezultats.config(text=f"spiediens ir: {p} Pa")
    except ValueError:
        messagebox.showwarning("kluda","Ievadiet derīgus skaitļus")


tk.Label(logs, text="ievadi spēku (F):").pack(pady=10)
ievade_speks=tk.Entry(logs)
ievade_speks.pack()
tk.Label(logs, text="ievadi laukumu (S):").pack(pady=10)
ievade_speks=tk.Entry(logs)
ievade_speks.pack()
tk.Label(logs, text="ievadi spiedienu (p):").pack(pady=10)
ievade_laukums=tk.Entry(logs)
ievade_laukums.pack()
poga=tk.Button(logs, text="aprekinat spiedienu",
               command=aprekinat_spiedienu)
poga.pack(pady=10)
rezultats=tk.Label(logs, text="spiediens ir: ")
rezultats.pack(pady=10)













logs.mainloop()