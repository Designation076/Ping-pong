from pygame import *
class GameSprite(sprite.Sprite):
    #конструктор класса
       #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height): # добавить еще два параметра при создании и задавать размер прямоугольгника для картинки самим
        super().__init__()
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (wight, height)) # вместе 55,55 - параметры
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

back = (200, 255, 255)
win_height = 500
win_width = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

speed_x = 1
speed_y = 1
game = True
finish = False
clock = time.Clock()
FPS = 60

racket_r = Player("p1.png", 30, 200, 4, 25, 75)
racket_l = Player("p2.png", 420, 200, 4, 25, 75)
ball = GameSprite("Ball.png", 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(back)
        racket_r.update_r()
        racket_l.update_l()

        if ball.rect.y < 0 or ball.rect.y > 450:
            speed_y *= -1
        
        if sprite.collide_rect(racket_l, ball) or sprite.collide_rect(racket_r, ball):
            speed_x *= -1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        racket_r.reset()
        racket_l.reset()
        ball.reset()
    
    display.update()
    clock.tick(FPS)