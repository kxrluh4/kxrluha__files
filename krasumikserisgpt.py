import tkinter as tk
from tkinter import messagebox
logs=tk.Tk()    
logs.geometry("400x350")
logs.title("krāsu mikseris")
def atjaunot_krasu():
    r=sarkans.get()
    g=zalais.get()
    b=zils.get()
    krasas_kods=f'#{r:02x}{g:02x}{b:02x}'
    krasas_paraugs.config(bg=krasas_kods)

def paradit_rgb():
    r=sarkans.get()
    g=zalais.get()
    b=zils.get()
    messagebox.showinfo("RGB vērtības", f"Sarkans: {r}\nZaļš: {g}\nZils: {b}")

sarkans=tk.Scale(logs, from_=0, to=255, orient="horizontal", label="sarkans (R)", command=lambda x: atjaunot_krasu())
sarkans.pack()
zilais=tk.Scale(logs, from_=0, to=255, orient="horizontal", label="zaļš (G)", command=lambda x: atjaunot_krasu())
zilais.pack()
zalais=tk.Scale(logs, from_=0, to=255, orient="horizontal", label="zils (B)", command=lambda x: atjaunot_krasu())
zalais.pack()

krasu_paraugs=tk.Label(logs, text="krāsas paraugs", bg="#000000", fg="white", height=4)
krasu_paraugs.pack(fill="both", expand=True, pady=10)


poga = tk.Button(logs, text="Parādīt RGB vērtības", command=paradit_rgb)
poga.pack(pady=10)



logs.mainloop()
