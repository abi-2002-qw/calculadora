##vanessa abigail alvarado elizalde ##
##hacer una calculadora en color rosita /*-+
####con interfas grafica ##
import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# ventana visual donde mostrara  la parte grafica 
root = tk.Tk()
root.title("Calculadora")
root.configure(bg="#ffc0cb")  ##fondo rosita  ffc0cb

###crear un cuadro de entrada
entry = tk.Entry(root, width=20, font=("Arial", 24), bd=10, insertwidth=2, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# botones disponibles que tendra nuestra calculadora rosada ###
buttons = [###asi van a estar ordenados en nuetra tabla 
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+",
]

row_val = 1
col_val = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20, font=("Arial", 18), bg="#ffb6c1", command=lambda text=button_text: on_click(text))
    button.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# iniciar el bucle principal de la interfaz gráfica
root.mainloop()
