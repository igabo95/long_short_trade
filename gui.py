import tkinter as tk
from calculations import on_submit

def create_long_position_window(root):
    # Dizionario per memorizzare i campi di input
    entries = {}

    # Etichette e campi di input
    tk.Label(root, text="My Position's Capital:", bg='black', fg='white').grid(row=1, column=0, sticky='e', padx=5, pady=5)
    entries['capital'] = tk.Entry(root)
    entries['capital'].grid(row=1, column=1, padx=5, pady=5)

    tk.Label(root, text="Current Asset Price:", bg='black', fg='white').grid(row=2, column=0, sticky='e', padx=5, pady=5)
    entries['asset_price'] = tk.Entry(root)
    entries['asset_price'].grid(row=2, column=1, padx=5, pady=5)

    tk.Label(root, text="Top Price Prediction:", bg='black', fg='white').grid(row=3, column=0, sticky='e', padx=5, pady=5)
    entries['top_prediction'] = tk.Entry(root)
    entries['top_prediction'].grid(row=3, column=1, padx=5, pady=5)

    tk.Label(root, text="Wanted Liquidation Price:", bg='black', fg='white').grid(row=4, column=0, sticky='e', padx=5, pady=5)
    entries['liquidation_price'] = tk.Entry(root)
    entries['liquidation_price'].grid(row=4, column=1, padx=5, pady=5)

    # Caselle di testo per i risultati
    results = {}
    
    tk.Label(root, text="Liquidation Percentage:", bg='black', fg='white').grid(row=6, column=0, sticky='e', padx=5, pady=5)
    results['liquidation_percentage'] = tk.Entry(root, state='readonly')
    results['liquidation_percentage'].grid(row=6, column=1, padx=5, pady=5)

    tk.Label(root, text="Leverage:", bg='black', fg='white').grid(row=7, column=0, sticky='e', padx=5, pady=5)
    results['leverage'] = tk.Entry(root, state='readonly')
    results['leverage'].grid(row=7, column=1, padx=5, pady=5)

    tk.Label(root, text="Real Position Capital:", bg='black', fg='white').grid(row=8, column=0, sticky='e', padx=5, pady=5)
    results['real_position_capital'] = tk.Entry(root, state='readonly')
    results['real_position_capital'].grid(row=8, column=1, padx=5, pady=5)

    tk.Label(root, text="Profit Percent %:", bg='black', fg='white').grid(row=9, column=0, sticky='e', padx=5, pady=5)
    results['profit_percent'] = tk.Entry(root, state='readonly')
    results['profit_percent'].grid(row=9, column=1, padx=5, pady=5)

    tk.Label(root, text="Profit:", bg='black', fg='white').grid(row=10, column=0, sticky='e', padx=5, pady=5)
    results['profit'] = tk.Entry(root, state='readonly')
    results['profit'].grid(row=10, column=1, padx=5, pady=5)

    # Pulsante di invio
    submit_button = tk.Button(root, text="Submit", command=lambda: on_submit(entries, results))
    submit_button.grid(row=5, column=0, columnspan=2, pady=20)