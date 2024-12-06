import tkinter as tk
from PIL import Image, ImageTk
from calculations import on_submit

def create_long_position_window(root):
    # Carica l'immagine
    img = Image.open("short.png")  # Assicurati che l'immagine si trovi nella root directory
    ratio = float(img.size[1]) / float(img.size[0])
    image_width = 600
    img = img.resize((int(image_width), int(image_width*ratio)))  # Ridimensiona l'immagine
    photo = ImageTk.PhotoImage(img)

    # Crea un'etichetta per visualizzare l'immagine
    img_label = tk.Label(root, image=photo)
    img_label.image = photo  # Mantieni un riferimento all'immagine
    img_label.grid(row=11, column=0, columnspan=2, pady=10)  # Posiziona l'immagine nella griglia
    
    # Dizionario per memorizzare i campi di input
    entries = {}

    # Etichette e campi di input
    tk.Label(root, text="My Position initial Capital\t\tCi =", bg='black', fg='white').grid(row=1, column=0, sticky='e', padx=5, pady=5)
    entries['capital'] = tk.Entry(root)
    entries['capital'].grid(row=1, column=1, padx=5, pady=5)

    tk.Label(root, text="Current Asset Price\t\tP0 =", bg='black', fg='white').grid(row=2, column=0, sticky='e', padx=5, pady=5)
    entries['asset_price'] = tk.Entry(root)
    entries['asset_price'].grid(row=2, column=1, padx=5, pady=5)

    tk.Label(root, text="Bottom Price Prediction\t\tPt =", bg='black', fg='white').grid(row=3, column=0, sticky='e', padx=5, pady=5)
    entries['bottom_prediction'] = tk.Entry(root)
    entries['bottom_prediction'].grid(row=3, column=1, padx=5, pady=5)

    tk.Label(root, text="Wanted Liquidation Price\t\tPl =", bg='black', fg='white').grid(row=4, column=0, sticky='e', padx=5, pady=5)
    entries['liquidation_price'] = tk.Entry(root)
    entries['liquidation_price'].grid(row=4, column=1, padx=5, pady=5)

    # Caselle di testo per i risultati
    results = {}
    
    tk.Label(root, text="Liquidation Percentage\t\tPl% =", bg='black', fg='white').grid(row=6, column=0, sticky='e', padx=5, pady=5)
    results['liquidation_percentage'] = tk.Entry(root, state='readonly')
    results['liquidation_percentage'].grid(row=6, column=1, padx=5, pady=5)

    tk.Label(root, text="Leverage\t\t\t\tLx =", bg='black', fg='white').grid(row=7, column=0, sticky='e', padx=5, pady=5)
    results['leverage'] = tk.Entry(root, state='readonly')
    results['leverage'].grid(row=7, column=1, padx=5, pady=5)

    tk.Label(root, text="Real Position Capital\t\tCp =", bg='black', fg='white').grid(row=8, column=0, sticky='e', padx=5, pady=5)
    results['real_position_capital'] = tk.Entry(root, state='readonly')
    results['real_position_capital'].grid(row=8, column=1, padx=5, pady=5)

    tk.Label(root, text="Profit Percent\t\t\tY% =", bg='black', fg='white').grid(row=9, column=0, sticky='e', padx=5, pady=5)
    results['profit_percent'] = tk.Entry(root, state='readonly')
    results['profit_percent'].grid(row=9, column=1, padx=5, pady=5)

    tk.Label(root, text="Profit\t\t\t\tY =", bg='black', fg='white').grid(row=10, column=0, sticky='e', padx=5, pady=5)
    results['profit'] = tk.Entry(root, state='readonly')
    results['profit'].grid(row=10, column=1, padx=5, pady=5)

    # Pulsante di invio
    submit_button = tk.Button(root, text="Submit", command=lambda: on_submit(entries, results))
    submit_button.grid(row=5, column=0, columnspan=2, pady=20)