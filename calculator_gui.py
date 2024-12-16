import tkinter as tk

# Funzione per aggiornare l'input sul display
def button_click(value):
    current = display.get()
    display.set(current + value)

# Funzione per eseguire il calcolo
def calculate(event=None):  # Aggiunto parametro event per gestire l'evento di pressione del tasto Invio
    try:
        result = eval(display.get())  # Usa eval per calcolare l'espressione
        display.set(result)
    except:
        display.set("Error")

# Funzione per cancellare l'input
def clear():
    display.set("")

# Funzione per rimuovere l'ultimo carattere
def backspace():
    current = display.get()
    display.set(current[:-1])

# Crea la finestra principale
window = tk.Tk()
window.title("Calculator")
window.geometry("300x500")  # Aumentato l'altezza della finestra
window.resizable(False, False)

# Display (campo di testo per l'input e il risultato)
display = tk.StringVar()
entry = tk.Entry(window, textvariable=display, font=("Arial", 20), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="ew", padx=10, pady=10)

# Definiamo i pulsanti
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Aggiungi i pulsanti alla finestra
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(window, text=text, font=("Arial", 20), command=calculate)
    else:
        button = tk.Button(window, text=text, font=("Arial", 20), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col, ipadx=20, ipady=20, sticky="nsew")

# Aggiungi pulsanti per funzionalità extra
button_clear = tk.Button(window, text="C", font=("Arial", 20), command=clear)
button_clear.grid(row=5, column=0, ipadx=20, ipady=20, sticky="nsew")

button_backspace = tk.Button(window, text="←", font=("Arial", 20), command=backspace)
button_backspace.grid(row=5, column=1, ipadx=20, ipady=20, sticky="nsew")

# Imposta la gestione della griglia per espandere i pulsanti
for i in range(6):
    window.grid_rowconfigure(i, weight=1)
for j in range(4):
    window.grid_columnconfigure(j, weight=1)

# Associa il tasto Invio al calcolo
entry.bind("<Return>", calculate)

# Esegui la finestra
window.mainloop()
