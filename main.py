import tkinter as tk
from gui import create_long_position_window

def main():
    # Creazione della finestra principale
    root = tk.Tk()
    root.title("Crypto Futures GUI")
    
    # Imposta il colore di sfondo della finestra
    root.configure(bg='black')

    # Creazione di un'etichetta
    label = tk.Label(root, text="Long Position", font=("Arial", 24), bg='black', fg='white')
    label.grid(row=0, column=0, columnspan=2, pady=20)

    # Create main Window
    create_long_position_window(root)

    # Avvio del loop principale della GUI
    root.mainloop()

if __name__ == "__main__":
    main()