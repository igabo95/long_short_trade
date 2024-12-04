import tkinter as tk
from tkinter import messagebox

def open_choice_window():
    """Apre la finestra per scegliere tra Long e Short."""
    choice_window = tk.Tk()  # Crea una nuova finestra principale
    choice_window.title("Choose Position")

    tk.Label(choice_window, text="Select Position Type:", font=("Arial", 16)).pack(pady=20)

    long_button = tk.Button(choice_window, text="Long", command=lambda: [choice_window.destroy(), open_position_window("Long")])
    long_button.pack(pady=10)

    short_button = tk.Button(choice_window, text="Short", command=lambda: [choice_window.destroy(), open_position_window("Short")])
    short_button.pack(pady=10)

    choice_window.mainloop()  # Avvia il loop principale della finestra di scelta
    
def validate_positive_number(input_value):
    """Controlla se l'input è un numero positivo."""
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
        top_prediction = float(entries['top_prediction'].get())
        liquidation_price = float(entries['liquidation_price'].get())

        # Calcoli
        liquidation_percentage = 1 - (liquidation_price / asset_price)
        leverage = 1.0 / liquidation_percentage
        real_position_capital = capital * leverage
        profit_percent = top_prediction/asset_price
        profit = real_position_capital * ( profit_percent - 1 )

        # Aggiorna le caselle di testo
        liquidation_percentage_entry.config(state='normal')  # Abilita la modifica
        liquidation_percentage_entry.delete(0, tk.END)
        liquidation_percentage_entry.insert(0, f"{liquidation_percentage:.2%}")
        liquidation_percentage_entry.config(state='readonly')  # Rendi di nuovo sola lettura

        leverage_entry.config(state='normal')  # Abilita la modifica
        leverage_entry.delete(0, tk.END)
        leverage_entry.insert(0, f"x{leverage:.2f}")
        leverage_entry.config(state='readonly')  # Rendi di nuovo sola lettura

        real_position_capital_entry.config(state='normal')  # Abilita la modifica
        real_position_capital_entry.delete(0, tk.END)
        real_position_capital_entry.insert(0, f"{real_position_capital:.2f} USD")
        real_position_capital_entry.config(state='readonly')  # Rendi di nuovo sola lettura

        profit_percent_entry.config(state='normal')  # Abilita la modifica
        profit_percent_entry.delete(0, tk.END)
        profit_percent_entry.insert(0, f"{profit_percent:.2%}")
        profit_percent_entry.config(state='readonly')  # Rendi di nuovo sola lettura

        profit_entry.config(state='normal')  # Abilita la modifica
        profit_entry.delete(0, tk.END)
        profit_entry.insert(0, f"{profit:.2f} USD")
        profit_entry.config(state='readonly')  # Rendi di nuovo sola lettura

    except ZeroDivisionError:
        messagebox.showerror("Errore", "Il Liquidation Price non può essere zero.")
    except Exception as e:
        messagebox.showerror("Errore", str(e))

def on_submit(entries):
    """Funzione chiamata quando si preme il pulsante di invio."""
    if (validate_positive_number(entries['capital'].get()) and 
        validate_positive_number(entries['asset_price'].get()) and 
        int(entries['liquidation_price'].get()) < int(entries['asset_price'].get()) and
        int(entries['asset_price'].get()) < int(entries['top_prediction'].get())):
        calculate_values(entries)
    else:
        messagebox.showerror("Input Non Valido", "Assicurati di inserire solo numeri positivi.")

def open_position_window(position_type):
    # Apre la finestra per la posizione Long o Short
    position_window = tk.Toplevel()
    position_window.title(f"{position_type} Position")
    
    # Imposta il colore di sfondo della finestra
    position_window.configure(bg='black')

    # Creazione di un'etichetta con il testo "Hello, World!"
    label = tk.Label(position_window, text="Buy Low -> Sell high", font=("Arial", 18), bg='black', fg='white')
    label.grid(row=0, column=0, columnspan=2, pady=20)

    # Dizionario per memorizzare i campi di input
    entries = {}

    # Etichette e campi di input
    tk.Label(position_window, text="My Position's Capital:", bg='black', fg='white').grid(row=1, column=0, sticky='e', padx=5, pady=5)
    entries['capital'] = tk.Entry(position_window)
    entries['capital'].grid(row=1, column=1, padx=5, pady=5)

    tk.Label(position_window, text="Current Asset Price:", bg='black', fg='white').grid(row=2, column=0, sticky='e', padx=5, pady=5)
    entries['asset_price'] = tk.Entry(position_window)
    entries['asset_price'].grid(row=2, column=1, padx=5, pady=5)

    tk.Label(position_window, text="Top Price Prediction:", bg='black', fg='white').grid(row=3, column=0, sticky='e', padx=5, pady=5)
    entries['top_prediction'] = tk.Entry(position_window)
    entries['top_prediction'].grid(row=3, column=1, padx=5, pady=5)

    tk.Label(position_window, text="Wanted Liquidation Price:", bg='black', fg='white').grid(row=4, column=0, sticky='e', padx=5, pady=5)
    entries['liquidation_price'] = tk.Entry(position_window)
    entries['liquidation_price'].grid(row=4, column=1, padx=5, pady=5)

    # Pulsante di invio
    submit_button = tk.Button(position_window, text="Submit", command=lambda: on_submit(entries))
    submit_button.grid(row=5, column=0, columnspan=2, pady=20)

    # Caselle di testo per i risultati
    tk.Label(position_window, text="Liquidation Percentage:", bg='black', fg='white').grid(row=6, column=0, sticky='e', padx=5, pady=5)
    global liquidation_percentage_entry
    liquidation_percentage_entry = tk.Entry(position_window, state='readonly')
    liquidation_percentage_entry.grid(row=6, column=1, padx=5, pady=5)

    tk.Label(position_window, text="Leverage:", bg='black', fg='white').grid(row=7, column=0, sticky='e', padx=5, pady=5)
    global leverage_entry
    leverage_entry = tk.Entry(position_window, state='readonly')
    leverage_entry.grid(row=7, column=1, padx=5, pady=5)

    tk.Label(position_window, text="Real Position Capital:", bg='black', fg='white').grid(row=8, column=0, sticky='e', padx=5, pady=5)
    global real_position_capital_entry
    real_position_capital_entry = tk.Entry(position_window, state='readonly')
    real_position_capital_entry.grid(row=8, column=1, padx=5, pady=5)

    tk.Label(position_window, text="Profit Percent %:", bg='black', fg='white').grid(row=9, column=0, sticky='e', padx=5, pady=5)
    global profit_percent_entry
    profit_percent_entry = tk.Entry(position_window, state='readonly')
    profit_percent_entry.grid(row=9, column=1, padx=5, pady=5)

    tk.Label(position_window, text="Profit:", bg='black', fg='white').grid(row=10, column=0, sticky='e', padx=5, pady=5)
    global profit_entry
    profit_entry = tk.Entry(position_window, state='readonly')
    profit_entry.grid(row=10, column=1, padx=5, pady=5)

    # Avvio del loop principale della GUI
    position_window.mainloop()

def main():
    root = tk.Tk()  # Crea la finestra principale
    root.withdraw()  # Nascondi la finestra principale
    open_choice_window()  # Inizializza la finestra di scelta
    root.mainloop()  # Avvia il loop principale della finestra principale

if __name__ == "__main__":
    main()