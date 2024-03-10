from pygame import*
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Maze')
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

game = True #щоб гра відкривлась/закривалась
clock = time.Clock() #частота кадрів
FPS = 60
class GameSprite(sprite.Sprite): #загальні характеристики персонажів
    def __init__(self,player_image, player_x, player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65)) #зображення персонажів
        self.speed = player_speed
        self.rect = self.image.get_rect() #невидима обводка чи стикнулись персонажі
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self): #на екран персонажа
        window.blit(self.image, ( self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 3:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width -70:
            self.rect.x += self.speed
            if keys[K_UP] and self.rect.y > 3:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < win_width -70:
                self.rect.y += self.speed
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


player = Player('картинка персонажа',5, win_height - 80,4)
monster = Enemy('монстр', win_width - 80,280,3)
goal = GameSprite('скарб', 440,420,0)
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
while game:
    for e in event.get(): #щоб віконце не зависало
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))
    player.update()
    monster.update()
    goal.reset()
    player.reset() #відобразити героя
    monster.reset()
    display.update()
    clock.tick(FPS) #частота кадрів