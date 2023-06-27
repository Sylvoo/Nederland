import pgzrun
from random import randint, choice

# KLASA PALETKI
class Palette:
    def __init__(self, palette, position, width=140, ball_width=10 ):
        self.palette = palette
        self.palette.x = position[0]
        self.palette.y = position[1]
        self.palette.speed = 5
        self.palette.pcenter = width//2
        self.palette.ball_width = ball_width
    def drawing(self):
        self.palette.draw()
    def move(self, direction):
        if direction == "left":
            self.palette.x -= self.palette.speed
            if self.palette.x < self.palette.pcenter:
                self.palette.x = self.palette.pcenter + 5
        elif direction == "right":
            self.palette.x += self.palette.speed
            if self.palette.x > (WIDTH - self.palette.pcenter):
                self.palette.x = WIDTH - self.palette.pcenter + 5
    def bounce(self):
        if self.palette.distance_to(ball) > self.palette.pcenter + self.palette.ball_width:
            return False

        if abs(self.palette.y - ball.y) > self.palette.ball_width * 2:
            return False

        if self.palette.x > ball.x and ball.direction_x == "left":
            ball.direction_x = "right"
        elif self.palette.x < ball.x and ball.direction_x == "right":
            ball.direction_x = "left"

        return True