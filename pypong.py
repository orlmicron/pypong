from tkinter import Tk, Canvas
import time

from ball import Pelota
from raqueta import Raqueta, Puntuacion


def main():
    tk = Tk()
    tk.title("PyPong")
    tk.resizable(0,0)
    tk.wm_attributes("-topmost", 1)
    canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
    canvas.pack()
    tk.update()

    puntuacion = Puntuacion(canvas, "black")
    raqueta = Raqueta(canvas, "blue")
    pelota = Pelota(canvas, raqueta, puntuacion, 'red')
    game_over_text = canvas.create_text(250, 200, font=("Ubuntu", 34),
                                        text="Fin del Juego", state="hidden")

    while True:
        if not pelota.golpea_fondo and pelota.play:
            pelota.dibujar()
            raqueta.dibujar()
        elif pelota.golpea_fondo:
            time.sleep(0.3)
            canvas.itemconfig(game_over_text, state="normal")
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
