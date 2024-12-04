import tkinter as tk
from tkinter import messagebox

def validate_positive_number(input_value):
    """Controlla se l'input è un numero positivo."""
    if input_value == "":
        return True  # Permetti input vuoto
    try:
        value = float(input_value)
        return value > 0  # Controlla se il numero è positivo
    except ValueError:
        return False  # Non è un numero valido

def on_submit(entries):
    """Funzione chiamata quando si preme il pulsante di invio."""
    capital = entries['capital'].get()
    asset_price = entries['asset_price'].get()
    liquidation_price = entries['liquidation_price'].get()

    if (validate_positive_number(capital) and 
        validate_positive_number(asset_price) and 
        validate_positive_number(liquidation_price)):
        messagebox.showinfo("Input Valido", "Tutti i valori sono validi!")
    else:
        messagebox.showerror("Input Non Valido", "Assicurati di inserire solo numeri positivi.")

def main():
    # Creazione della finestra principale
    root = tk.Tk()
    root.title("Crypto Futures GUI")
    
    # Imposta il colore di sfondo della finestra
    root.configure(bg='black')

    # Creazione di un'etichetta con il testo "Hello, World!"
    label = tk.Label(root, text="Hello, World!", font=("Arial", 24), bg='black', fg='white')
    label.pack(pady=20)

    # Dizionario per memorizzare i campi di input
    entries = {}

    # Etichette e campi di input
    tk.Label(root, text="My Capital:", bg='black', fg='white').pack(pady=5)
    entries['capital'] = tk.Entry(root)
    entries['capital'].pack(pady=5)

    tk.Label(root, text="Current Asset Price:", bg='black', fg='white').pack(pady=5)
    entries['asset_price'] = tk.Entry(root)
    entries['asset_price'].pack(pady=5)

    tk.Label(root, text="Wanted Liquidation Price:", bg='black', fg='white').pack(pady=5)
    entries['liquidation_price'] = tk.Entry(root)
    entries['liquidation_price'].pack(pady=5)

    # Pulsante di invio
    submit_button = tk.Button(root, text="Submit", command=lambda: on_submit(entries))
    submit_button.pack(pady=20)

    # Avvio del loop principale della GUI
    root.mainloop()

if __name__ == "__main__":
    main()