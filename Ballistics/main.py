import pygame
import random
#константы
width=600
height=400
w=50
h=50
FPS=60
#цвета
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green1=(191,255,0)
green2=(255,223,132)
blue=(0,0,255)
#переменные
x=(width-w)/2
y=(height-h)/2
mg=20
rl=5
#классы
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf=pygame.Surface((w,h))
        self.surf.fill(green2)
        self.rect=self.surf.get_rect()
        self.rect.center=(x,y)

    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y>25:
            self.rect.y -=3
        if keys[pygame.K_s] and self.rect.y<(height-h):
            self.rect.y +=3
        if keys[pygame.K_a] and self.rect.x>0:
            self.rect.x -=3
        if keys[pygame.K_d] and self.rect.x<(width-w):
            self.rect.x +=3
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf=pygame.Surface((30,15))
        self.surf.fill(red)
        self.rect=self.surf.get_rect(
            center=(
                random.randint(width+20,width+100),
                random.randint(0,height),
            )
        )
        self.speed=random.randint(5,20)
    
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right<0:
            self.kill()
#установки
pygame.mixer.init()
pygame.init()

ADDENEMY=pygame.USEREVENT+1
pygame.time.set_timer(ADDENEMY,1000)

win=pygame.display.set_mode((width,height))
pygame.display.set_caption("igrulya")

pygame.mixer.music.load("Record.wav")
pygame.mixer.music.set_volume(0.08)
pygame.mixer.music.play(loops=-1)
clock=pygame.time.Clock()
enemies=pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
player=Player()

all_sprites.add(player)
all_sprites.add(enemies)

#игровой цикл
while True:
    win.fill(blue)
    #частота кадров
    clock.tick(FPS)
    #выход
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type==ADDENEMY:
            new_enemy=Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    #отрисовка
    for entity in all_sprites:
        win.blit(entity.surf, entity.rect)
    if pygame.sprite.spritecollideany(player,enemies):
        player.kill()



    #обновление
    all_sprites.update()
    pygame.display.update()



