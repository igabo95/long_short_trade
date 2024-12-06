import tkinter as tk
from tkinter import messagebox

def on_submit(entries, results):
    """Funzione chiamata quando si preme il pulsante di invio."""
    if (validate_positive_number(entries['capital'].get()) and 
        validate_positive_number(entries['asset_price'].get()) and 
        int(entries['liquidation_price'].get()) < int(entries['asset_price'].get()) and
        int(entries['asset_price'].get()) < int(entries['top_prediction'].get())):
        calculate_values(entries, results)
    else:
        messagebox.showerror("Input Non Valido", "Assicurati di inserire solo numeri positivi.")

def validate_positive_number(input_value):
    """Controlla se l'input è un numero positivo."""
    try:
        value = float(input_value)
        return value > 0  # Controlla se il numero è positivo
    except ValueError:
        return False  # Non è un numero valido

def calculate_values(entries, results):
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
        profit = real_position_capital * (top_prediction / asset_price) - real_position_capital
        profit_percent = profit / capital

        # Aggiorna le caselle di testo
        results['liquidation_percentage'].config(state='normal')  # Abilita la modifica
        results['liquidation_percentage'].delete(0, tk.END)
        results['liquidation_percentage'].insert(0, f"-{liquidation_percentage:.2%}")
        results['liquidation_percentage'].config(state='readonly')  # Rendi di nuovo sola lettura

        results['leverage'].config(state='normal')  # Abilita la modifica
        results['leverage'].delete(0, tk.END)
        results['leverage'].insert(0, f"x{leverage:.2f}")
        results['leverage'].config(state='readonly')  # Rendi di nuovo sola lettura

        results['real_position_capital'].config(state='normal')  # Abilita la modifica
        results['real_position_capital'].delete(0, tk.END)
        results['real_position_capital'].insert(0, f"{real_position_capital:.2f} USD")
        results['real_position_capital'].config(state='readonly')  # Rendi di nuovo sola lettura

        results['profit_percent'].config(state='normal')  # Abilita la modifica
        results['profit_percent'].delete(0, tk.END)
        results['profit_percent'].insert(0, f"{profit_percent:.2%}")
        results['profit_percent'].config(state='readonly')  # Rendi di nuovo sola lettura

        results['profit'].config(state='normal')  # Abilita la modifica
        results['profit'].delete(0, tk.END)
        results['profit'].insert(0, f"{profit:.2f} USD")
        results['profit'].config(state='readonly')  # Rendi di nuovo sola lettura

    except ZeroDivisionError:
        messagebox.showerror("Errore", "Il Liquidation Price non può essere zero.")
    except Exception as e:
        messagebox.showerror("Errore", str(e))