from tkinter import Tk, Canvas
import random
import time


class Pelota:
    def __init__(self, canvas, raqueta, puntuacion, color):
        self.canvas = canvas
        self.raqueta = raqueta
        self.puntuacion = puntuacion
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        start = [-3, -2, -1, 1, 2, 3]
        self.speed = 3
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.golpea_fondo = False
        self.play = False
        self.canvas.bind_all("<Button-1>", self.pause)

    def pause(self, evt):
        self.play = not self.play

    def golpe_raqueta(self, pos):
        raqueta_pos = self.canvas.coords(self.raqueta.id)
        if pos[2] >= raqueta_pos[0] and pos[0] <= raqueta_pos[2]:
            if pos[3] >= raqueta_pos[1] and pos[3] <= raqueta_pos[3]:
                self.x += self.raqueta.x
                self.puntuacion.tanto()
                # self.canvas.
                return True
        return False

    def dibujar(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = self.speed
        if pos[3] >= self.canvas_height:
            self.golpea_fondo = True
        if self.golpe_raqueta(pos):
            self.y = -self.speed
        if pos[0] <= 0:
            self.x = self.speed
        if pos[2] >= self.canvas_width:
            self.x = -self.speed


class Raqueta:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0 , 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.ir_izq)
        self.canvas.bind_all("<KeyPress-Right>", self.ir_der)

    def dibujar(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] == 0:
            self.x = 0
        elif pos[0] < 0:
            self.x = 1
        elif pos[2] == self.canvas_width:
            self.x = 0
        elif pos[2] > self.canvas_width:
            self.x = -1

    def ir_izq(self, evt):
        self.x = -2

    def ir_der(self, evt):
        self.x = 2


class Puntuacion:
    def __init__(self, canvas, color):
        self.puntuacion = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 25, font=("Ubuntu", 34),
                                     text=self.puntuacion, fill=color)

    def tanto(self):
        self.puntuacion += 1
        self.canvas.itemconfig(self.id, text=self.puntuacion)

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
