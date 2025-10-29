# import tkinter as tk
# logs=tk.Tk()
# logs.geometry("400x350")
# logs.title("pirmais kalkulators")

# def saskaitit():
#     teksts1=teksts_2.get()
#     teksts2=teksts_4.get()

#     skaitlis1=int(teksts1)
#     skaitlis2=int(teksts2)

#     summa=skaitlis1+skaitlis2

#     label_rezultats.config(text=f"summa: {summa}")



# teksts_1=tk.Label(logs, text="pirmais skaitlis:",)

# teksts_2=tk.Entry(logs)


# teksts_3=tk.Label(logs, text="otrais skaitlis:",)

# teksts_4=tk.Entry(logs)

# poga1=tk.Button(logs,text="saskaitit", command=saskaitit)
# label_rezultats=tk.Label(logs, text="summa: ")


# teksts_1.pack()
# teksts_2.pack()
# teksts_3.pack()

# teksts_4.pack()
# poga1.pack(pady=10)
# label_rezultats.pack()  



# logs.mainloop()


import tkinter as tk
logs=tk.Tk()
logs.geometry("400x350")
logs.title("krāsu mainītājs")

def krasu_maina():
    krase=krasu_ievade.get()
    logs.config(bg=krase)

tk.Label(logs, text="ievadi krāsu nosaukumu angliski:").pack(pady=10)
poga=tk.Button(logs, text="mainit krāsu",
               command=krasu_maina)

krasu_ievade=tk.Entry(logs)
krasu_ievade.pack()
poga.pack(pady=10)


























logs.mainloop()



