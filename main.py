from database import setup_database
import gui

if __name__ == "__main__":
    setup_database()
    root = gui.tk.Tk()
    app = gui.PharmacyApp(root)
    root.mainloop()
