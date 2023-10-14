from random import *
from pygame import *

font.init()






background = transform.scale(image.load("image.jpg"), (700, 500))
font = font.Font('Arial', True, (50,50))
window = display.set_mode((700, 500))
clock = time.Clock()
game = True
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(player_image), (self.width, self.height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y <400:
            self.rect.y+=self.speed
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y-= self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y <400:
            self.rect.y+=self.speed
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y-= self.speed
player1 = Player('racket.png', 10, 0,250, 30,100)
player2 = Player('racket.png', 10, 665, 250, 30, 100)
ball = GameSprite('tenis_ball.png', 10, 0, 0,50,50)
speed_x = 5
speed_y = 5  
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        player1.reset()
        player1.update_l()
        player2.reset()
        player2.update_r()
        ball.reset()
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y
    if sprite.collide_rect(player1, ball):
        speed_x*=-1

    if sprite.collide_rect(player2, ball):
        speed_x*=-1

    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1
    if ball.rect.x >= 700:
        window.blit(win1, (350,250))
    if ball.rect.x <=0:
        window.blit(win2, (350,250))
    clock.tick(60)
    display.update()
