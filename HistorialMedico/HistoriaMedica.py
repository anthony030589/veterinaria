import tkinter as tk
from Mascota.gui import Frame
def main():
    ventanaHistoriaM = tk.Tk()
    ventanaHistoriaM.title('Historia Medica')
    ventanaHistoriaM.resizable(0,0)

    frame = Frame(ventanaHistoriaM)
    frame.mainloop()

if __name__ == '__main__':
    main()