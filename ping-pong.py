from pygame import*
from time import sleep

background = (50, 205, 50)
window = display.set_mode((900, 600))
display.set_caption('Пинг-Понг')

class GameSprite(sprite.Sprite):
    def __init__(self, img, x_pus, y_pus, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(img),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x_pus
        self.rect.y = y_pus
        self.speed = speed
        self.width = width
        self.height = height

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        pressed = key.get_pressed()
        if pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if pressed[K_s] and self.rect.y < 500:
            self.rect.y += self.speed

    def update_r(self):
        pressed = key.get_pressed()
        if pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if pressed[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def __init__(self, colors, width, height, pos_x, pos_y):
        super().__init__()
        self.colors = colors
        self.width = width
        self.height =  height
        self.img = Surface((self.width, self.height))
        self.rect = self.img.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.img.fill(self.colors)

    def draw(self):
        window.blit(self.img, self.rect)

racket_1 = Player('racket.png', 30, 250, 10, 20, 100)
racket_2 = Player('racket.png', 850, 250, 10, 20, 100)
ball = GameSprite('ball.png', 450, 300, 4, 30, 30)
w1 = Wall((255,255,255), 10, 600, 440, 0)

game = True
finish = False
score1 = 0
score2 = 0
speed_x = 3
speed_y = 3

clock = time.Clock()
FPS = 60

font.init()
f = font.SysFont('verdana', 30)
win1 = f.render('Player1 WIN!!!', True, (0, 0, 0))
win2 = f.render('Player2 WIN!!!', True, (0, 0, 0))
lose1 = f.render('Player1 LOSE', True, (0, 0, 0))
lose2 = f.render('Player2 LOSE', True, (0, 0, 0))

while game:
    if not finish:
        window.fill(background)

        if sprite.collide_rect(racket_1, ball):
            speed_x *= -1
            score1 += 1

        if sprite.collide_rect(racket_2, ball):
            speed_x *= -1
            score2 += 1

        if ball.rect.y > 570 or ball.rect.y < 0:
            speed_y *= -1
            
        if ball.rect.x < 0:
            window.blit(lose1,(400, 200))
            finish = True

        if ball.rect.x > 900:
            window.blit(lose2,(400, 200))
            finish = True

        if finish:
            display.update()
            time.delay(3000)
            game = False

        if score1 == 10:
            window.blit(win1,(100, 200))

        if score2 == 10:
            window.blit(win2,(600, 200))

        racket_1.draw()
        racket_1.update_l()
        racket_2.draw()
        racket_2.update_r()
        w1.draw()
        ball.draw()
        ball.rect.y += speed_y
        ball.rect.x += speed_x

        score_text = f.render(f'{str(score1)}', True, (0, 0, 0))
        window.blit(score_text, (10, 10))

        score_text = f.render(f'{str(score2)}', True, (0, 0, 0))
        window.blit(score_text, (870, 10))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
