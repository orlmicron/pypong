import random


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