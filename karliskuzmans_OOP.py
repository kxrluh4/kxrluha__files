import tkinter as tk
from tkinter import messagebox
logs=tk.Tk()
logs.geometry("1000x800")
logs.title("spiediena aprekins")
logs.configure(bg="lightblue")
#izveidoju logu spiediena aprekins

def aprekinat_spiedienu():# aprēķina spiedienu pēc formulas p=F/S
    try:
        teksts1=ievade_speks.get()
        teksts2=ievade_laukums.get()

        F=speks=int(teksts1)
        A=laukums=int(teksts2)
        p=spiediens=F/A
        rezultats.config(text=f"spiediens ir: {p} Pa")
        if A==0:
            messagebox.showerror("kluda", "laukums nevar but nulle!!!")
        else:#ja laukums nav nulle, aprēķina spiedienu
            p=F/S
            rezultats.config(text=f"spiediens ir: {p} Pa")
    except ValueError:#pārbauda vai ievadītās vērtības ir skaitliskas
        messagebox.showerror("Kluda", "ievadi derigus skaitlus!")


tk.Label(logs, text="ievadi spēku (F):").pack(pady=10)
ievade_speks=tk.Entry(logs)
ievade_speks.pack()
tk.Label(logs, text="ievadi laukumu (A):").pack(pady=10)
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

attels=tk.PhotoImage(file="spiediens2.png")
etikets_attels=tk.Label(logs, image=attels, bg="lightblue")
etikets_attels.pack(pady=10)





logs.mainloop()