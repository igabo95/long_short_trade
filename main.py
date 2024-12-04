import tkinter as tk

def main():
    # Creazione della finestra principale
    root = tk.Tk()
    root.title("Hello World GUI")
    
    # Imposta il colore di sfondo della finestra
    root.configure(bg='black')

    # Creazione di un'etichetta con il testo "Hello, World!"
    label = tk.Label(root, text="Hello, World!", font=("Arial", 24), bg='black', fg='white')
    label.pack(pady=20)

    # Avvio del loop principale della GUI
    root.mainloop()

if __name__ == "__main__":
    main()