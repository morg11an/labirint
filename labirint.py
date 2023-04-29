import pygame 
v = 700 
h = 500
window = pygame.display.set_mode(( v , h ))
pygame.display.set_caption("Лабіринт")
background = pygame.transform.scale(pygame.image.load("fon.jpeg") , (v,h))
class Player(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image),(70,70))
        self.speed = player_speed
        self.rect = self.image.get_rect() #створити рамку навколо картинки спрайта
        self.rect.x = player_x 
        self.rect.y = player_y
    def reset(self): #функція для того щоб намалювати спрайт на екрані
        window.blit(self.image, (self.rect.x , self.rect.y))

hero = Player("tyu.png", 10,400, 40)
enemy = Player("hjk.png", 500, 70, 40)
skarb = Player("kvas.png", 500, 400, 0)

game = True
clock = pygame.time.Clock()
FPS = 60
while game:
    for a in pygame.event.get():
        if a.type == pygame.QUIT:
            game = False 
    window.blit(background, (0,0))
    hero.reset()
    enemy.reset()
    pygame.display.update()
    clock.tick(FPS)