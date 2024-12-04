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

def calculate_values(entries):
    """Calcola i valori e aggiorna le caselle di testo."""
    try:
        capital = float(entries['capital'].get())
        asset_price = float(entries['asset_price'].get())
        liquidation_price = float(entries['liquidation_price'].get())

        # Calcoli
        liquidation_percentage = 1 - (liquidation_price / asset_price)
        leverage = 1.0 / liquidation_percentage
        real_position_capital = capital * leverage

        # Aggiorna le caselle di testo
        liquidation_percentage_entry.config(state='normal')  # Abilita la modifica
        liquidation_percentage_entry.delete(0, tk.END)
        liquidation_percentage_entry.insert(0, f"{liquidation_percentage:.2%}")
        liquidation_percentage_entry.config(state='readonly')  # Rendi di nuovo sola lettura

        leverage_entry.config(state='normal')  # Abilita la modifica
        leverage_entry.delete(0, tk.END)
        leverage_entry.insert(0, f"{leverage:.2f}")
        leverage_entry.config(state='readonly')  # Rendi di nuovo sola lettura

        real_position_capital_entry.config(state='normal')  # Abilita la modifica
        real_position_capital_entry.delete(0, tk.END)
        real_position_capital_entry.insert(0, f"{real_position_capital:.2f}")
        real_position_capital_entry.config(state='readonly')  # Rendi di nuovo sola lettura

    except ZeroDivisionError:
        messagebox.showerror("Errore", "Il Liquidation Price non può essere zero.")
    except Exception as e:
        messagebox.showerror("Errore", str(e))

def on_submit(entries):
    """Funzione chiamata quando si preme il pulsante di invio."""
    if (validate_positive_number(entries['capital'].get()) and 
        validate_positive_number(entries['asset_price'].get()) and 
        validate_positive_number(entries['liquidation_price'].get())):
        calculate_values(entries)
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

    # Caselle di testo per i risultati
    tk.Label(root, text="Liquidation Percentage:", bg='black', fg='white').pack(pady=5)
    global liquidation_percentage_entry
    liquidation_percentage_entry = tk.Entry(root, state='readonly')
    liquidation_percentage_entry.pack(pady=5)

    tk.Label(root, text="Leverage:", bg='black', fg='white').pack(pady=5)
    global leverage_entry
    leverage_entry = tk.Entry(root, state='readonly')
    leverage_entry.pack(pady=5)

    tk.Label(root, text="Real Position Capital:", bg='black', fg='white').pack(pady=5)
    global real_position_capital_entry
    real_position_capital_entry = tk.Entry(root, state='readonly')
    real_position_capital_entry.pack(pady=5)

    # Avvio del loop principale della GUI
    root.mainloop()

if __name__ == "__main__":
    main()