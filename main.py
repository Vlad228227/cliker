import pygame
import pygame as pg
pygame.init()
window = pygame.display.set_mode((632, 475))
run = True
coins = 0
bg = pygame.image.load('images/bg.png')
def draw(img, x, y):
    window.blit(img, (x, y))

class mr_click:
    cost = 50
    per_sec = 0.1
    amount = 0
    img = pygame.image.load('images/MrClick.svg')
    def when_clicked(self, coins):
        if coins >= self.cost:
            self.amount += 1
            self.cost += 2
f1 = pygame.font.Font(None, 36)
# if (pos_x > person_x) and (pos_x < person_x + 80) and
# (pos_y > person_y) and (pos_y < person_y + 80) and pause == False:
class Coin_upgr():
    img = pygame.image.load("images/upgrade.svg")
    cost = 150
    def when_clicked(self, coin, coins):
        if coins >= self.cost and coin.upgrade_line < 4:
            self.cost += 420
            coin.upgrade()
class mario():
    cost = 100
    per_sec = 0.5
    amount = 0
    img = pygame.image.load('images/mario.png').convert_alpha()
    tcolor = img.get_at((0, 0))
    img.set_colorkey(tcolor)
    def when_clicked(self, coins):
        if coins >= self.cost:
            self.amount += 1
            self.cost += 2
class tree:
    cost = 350
    per_sec = 1
    amount = 0
    img = pygame.image.load('images/MrClick.svg')

    def when_clicked(self, coins):
        if coins >= self.cost:
            self.amount += 1
            self.cost += 2
class Coin(pygame.sprite.Sprite):
    img = pygame.image.load('images/coin1.svg')
    x = 310
    y = 235
    w = 58
    h = 58
    per_click = 0.3
    upgrade_line = 0
    def upgrade(self):
        if self.upgrade_line == 0:
            self.img = pygame.image.load('images/coin2.svg')
            self.per_click = 0.5
            self.upgrade_line = 1
        elif self.upgrade_line == 1:
            self.img = pygame.image.load('images/coin3.svg')
            self.per_click = 1
            self.upgrade_line = 2
        elif self.upgrade_line == 2:
            self.img = pygame.image.load('images/coin4.svg')
            self.per_click = 2
            self.upgrade_line = 3
coin = Coin()
mario = mario()
mr_click = mr_click()
tree = tree()
iter = 0
while run:
    text1 = f1.render(str(coins), 1, (180, 0, 0))
    iter += 1
    pos = pygame.mouse.get_pos()
    pos_x = pos[0]
    pos_y = pos[1]
    draw(bg, 0, 0)
    draw(coin.img, 310, 235)
    draw(mario.img, 100, 350)
    draw(mr_click.img, 50, 350)
    draw(tree.img, 150, 350)
    pg.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and (pos_x > coin.x) and (pos_x < coin.x + coin.w) and (pos_y > coin.y) and (pos_y < coin.y + coin.h):
                coins += coin.per_click
                print(coins)
        elif event.type == pygame.MOUSEBUTTONDOWN and (pos_x > 100) and (pos_x < 100 + 89) and (pos_y > 350) and (pos_y < 350 + 89):
            mario.when_clicked(coins)
        elif event.type == pygame.MOUSEBUTTONDOWN and (pos_x > 50) and (pos_x < 50 + 89) and (pos_y > 350) and (pos_y < 350 + 89):
            mr_click.when_clicked(coins)
    if iter == 1000:
        coins += mario.amount * mario.per_sec
        coins += mr_click.amount * mr_click.per_sec
        coins += tree.amount * tree.per_sec
        print(coins)
pygame.quit()