from pygame import*
from random import randint
font.init()
font=font.font(None,36)

img_win=" "
img_los=" "
img_back=" "

img_bullet=" "
img_hero=" "
img_enemy=" "

score=0
goal=10
lost=0
max_lost=3

class GameSpirit(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_y,size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image=transform.scale(image.load(player_image),(size_x,size_y))
        self.speed=player_speed
        self.rect=self.image.gett_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(Gamespirite):
    def update(slef):
        keys=key.get.pressed()
        if keys[K_LEFT] and self.rect.x>5:
            self.rect.x=self.speed
        if keys[K_RIGHT] and self.rect.x<win.width-80:
            self.rect.x+=self.speed
    def fire(self):
        bullet=Bullet(img_bullet,self.rect.centerx,self.rect.top,15,20,-15)
        bullets.add(bullet)
class Enemy(Gamespirite):
    def update(self):
        self.rect.y+=self.speed
        global lost
        if self.rect.y>win_height:
            self.rect.x=randint(80, win_height-80)
            self.rect.y=0
            lost=lost+1
class Bullet(Gamesprite):
    def update(self):
        self.rect.y+=self.speed
        if self.rect.y<0:
            self.kill()

win_width=700
win_height=500
display.set_caption("shooter")
window=display.set_mode((win_width,win_height))
background=transform.scale(image.load(img_back),(win_width,win_height))
ship=Player(img_Hero,5,win_height-100, 80, 100, 10)
monster=sprite.Group()
for i in range(1,6):
    monsters.add(monster)
bullets=sprite.Group()
finish=False
Run=True
while run :
    if e.type==QUIT:
        run=False
    elif e.type==KEYDOWN
        if e.key==K_SPACE:
            ship.fire()
    if not finish:
        window.blit(background,(0,0))
        text=font.render("Score: "+str(score),1,(255,255,255))
        text_lsoe=font.render("Missed: "+str(lost).1,(255,255,255))
        ship.update()
        monsters.update()
        bullets.update()

        ship.reset()
        monsters.draw(window)
        bullets.draw(window)

        collides=sprite.groupcollide(monsters,bullets,True, True)
        for c in collide:
            score=score+1
            monsters=Enemy(img_enemy,randint(80,win_width-80),-40, 80, 50,randint(1,5))
            if sprite.spritecollide(ship,monsters,False) or lost>=max_lost:
                finish=True
            img=image.load(img_los)
            d=img.get_width()//img.get_height()
            window.fill(255,255,255)
            window.blit(transform.scale(img,(win_height*d,win_height)),(90,0))
            if score>=goal:
                finish=True
                img=img.load(img_win)
                window.fill(2255,255,255)
                window.blit(transform.scale(img,(win_width,win_height)),(0,0))
            display.update(50)