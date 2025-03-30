import pygame
import random
import time

pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Creating a game window

background = pygame.image.load('resources/AnimatedStreet.png')
running = True

clock = pygame.time.Clock()
FPS = 60 

player_img = pygame.image.load('resources/Player.png') # loading images
enemy_img = pygame.image.load('resources/Enemy.png')
coin_img = pygame.image.load('resources/coin.png')
coin_img = pygame.transform.scale(coin_img, (40, 40))
coin_amount = 0

background_music = pygame.mixer.music.load('resources/background.wav') # loading sound and music
crash_sound = pygame.mixer.Sound('resources/crash.wav')
coin_sound = pygame.mixer.Sound('resources/coin_collect_sound.mp3')

font = pygame.font.SysFont("Verdana", 60)
game_over = font.render("Game Over", True, "red") 

pygame.mixer.music.play(-1) # plays background music in a loop

PLAYER_SPEED = 5
ENEMY_SPEED = 7

class Player(pygame.sprite.Sprite): # Player sprite
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - self.rect.w // 2
        self.rect.y = HEIGHT - self.rect.h
    
    def move(self):
        global ENEMY_SPEED
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.move_ip(-PLAYER_SPEED, 0) # move left
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.move_ip(PLAYER_SPEED, 0) # move right
        if keys[pygame.K_s] and ENEMY_SPEED >= 7 or keys[pygame.K_DOWN] and ENEMY_SPEED >= 7: # breaks
            ENEMY_SPEED -= 0.1
        if keys[pygame.K_w] or keys[pygame.K_UP]: # speeding up
            ENEMY_SPEED += 0.2
        if self.rect.left < 0: # left border
            self.rect.left = 0
        if self.rect.right > WIDTH: # right border
            self.rect.right = WIDTH

class Enemy(pygame.sprite.Sprite): # Enemy sprite
    def __init__(self): 
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.generate_random_rect()
    
    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > HEIGHT: # if enemy going out of screen, he respawns
            self.generate_random_rect()
    
    def generate_random_rect(self):
        self.rect.x = random.randint(20, WIDTH - self.rect.w - 20)
        self.rect.y = random.randint(-130 , -90)

class Coin(pygame.sprite.Sprite): # Coin sprite
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.generate_random_rect()
    
    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > HEIGHT: # if coin going out of screen, it respawns
            self.generate_random_rect()

    def generate_random_rect(self):
        self.rect.x = random.randint(5, WIDTH - self.rect.w - 5)
        self.rect.y = -60

player = Player() # Sprites
enemy1 = Enemy() 
enemy2 = Enemy() 
enemy3 = Enemy()
coin = Coin() 

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

all_sprites.add([player, enemy1, enemy2, enemy3 ,coin]) # all sprites
enemy_sprites.add([enemy1, enemy2, enemy3]) # enemy sprites

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    coin_text = font.render(str(coin_amount), True, "black")
    game_over_coin = font.render(f"Coins: {coin_amount}", True, "green") # showing number of coins in game over
    screen.blit(background, (0, 0))
    screen.blit(coin_text, (315, 15)) # showing number of coins
    screen.blit(coin_img, (270, 35)) # Coin image around number of coins

    player.move()
    enemy1.move()
    enemy2.move()
    enemy3.move()
    coin.move()

    for entity in all_sprites: # placing all sprites in screen
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, enemy_sprites): # if player crashes to enemy
        crash_sound.play() # crash sound plays
        pygame.time.delay(1000)

        screen.fill("white") # screen fills white
        center_gameover = game_over.get_rect(center = (WIDTH // 2, HEIGHT // 2 - 60)) 
        center_gameovercoin = game_over_coin.get_rect(center = (WIDTH // 2, HEIGHT // 2 - 5))
        screen.blit(game_over, center_gameover) # in center of screen "GAME OVER"
        screen.blit(game_over_coin, center_gameovercoin) # and number of coins

        pygame.display.flip()

        time.sleep(2)
        running = False

    if pygame.sprite.collide_rect(enemy1, enemy2) or pygame.sprite.collide_rect(enemy1, enemy3): # if enemy1 spawns in another enemy, he respawns 
        enemy1.generate_random_rect()

    if pygame.sprite.collide_rect(enemy2, enemy3): # if enemy2 spawns in enemy3, he respawns 
        enemy2.generate_random_rect()
    
    if pygame.sprite.spritecollideany(coin, enemy_sprites): # if coin spawns in enemies, it respawns
        coin.generate_random_rect()
    
    if pygame.sprite.collide_rect(player, coin): # if player collects coin
        coin_sound.play() # coin sound plays
        coin.generate_random_rect()
        coin_amount += 1

    pygame.display.flip() # updates the screen
    clock.tick(FPS) # sets the FPS