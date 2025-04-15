import pygame
import random
import psycopg2
import time
from config import config

pygame.init()

params = config()
connection = psycopg2.connect(**params)
cursor = connection.cursor()

WIDTH, HEIGHT = 400, 400
BLOCK = 20
MAX_LEVEL = 7

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
font = pygame.font.SysFont('Consolas', 25)
clock = pygame.time.Clock()

def get_user():
    username = input("Enter your username: ").strip()
    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    if user:
        user_id = user[0]
        cursor.execute("SELECT MAX(level) FROM user_scores WHERE user_id = %s", (user_id,))
        level = cursor.fetchone()[0] or 0
    else:
        cursor.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cursor.fetchone()[0]
        connection.commit()
        level = 0
    return user_id, username, level

def save_game_state(user_id, level, score):
    cursor.execute(
        "INSERT INTO user_scores (user_id, level, score) VALUES (%s, %s, %s)",
        (user_id, level, score)
    )
    connection.commit()
    print(f"Game saved for level {level} and score {score}")

def draw_grid():
    for x in range(0, WIDTH, BLOCK):
        for y in range(0, HEIGHT, BLOCK):
            rect = pygame.Rect(x, y, BLOCK, BLOCK)
            pygame.draw.rect(screen, (50, 50, 50), rect, 1)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Wall:
    def __init__(self, level):
        self.body = []
        path = f"levels/level{level % MAX_LEVEL}.txt"
        with open(path, 'r') as f:
            for y, line in enumerate(f):
                for x, char in enumerate(line.strip()):
                    if char == '#':
                        self.body.append(Point(x, y))

    def draw(self):
        for point in self.body:
            rect = pygame.Rect(point.x * BLOCK, point.y * BLOCK, BLOCK, BLOCK)
            pygame.draw.rect(screen, (255, 0, 255), rect)

# Snake
def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, (0, 255, 0), (x, y, BLOCK - 1, BLOCK - 1))

def generate_food(snake, wall):
    while True:
        x = random.randrange(0, WIDTH, BLOCK)
        y = random.randrange(0, HEIGHT, BLOCK)
        # Check it's not in snake
        if (x, y) in snake:
            continue
        # Check it's not in wall
        in_wall = False
        for point in wall.body:
            if x == point.x * BLOCK and y == point.y * BLOCK:
                in_wall = True
                break
        if in_wall:
            continue
        return (x, y)

def draw_score(score, level):
    val = font.render(f"Score: {score}  Level: {level}", True, (255, 255, 255))
    screen.blit(val, (10, 10))

def pause(user_id, level, score):
    paused = True
    while paused:
        screen.fill((0, 0, 0))
        msg = font.render("Paused: S - Save  P - Play  Q - Quit", True, (255, 255, 255))
        screen.blit(msg, (20, HEIGHT // 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_s:
                    save_game_state(user_id, level, score)

def main():
    user_id, username, level = get_user()
    speed = 5 + level
    score = 0
    
    wall = Wall(level)

    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0
    snake = []
    length = 1

    food = generate_food(snake, wall)

    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_grid()
        wall.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -BLOCK, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = BLOCK, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -BLOCK
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, BLOCK
                elif event.key == pygame.K_ESCAPE:
                    pause(user_id, level, score)

        x += dx
        y += dy

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            break  # hit wall

        for block in snake[:-1]:
            if (x, y) == block:
                running = False  # hit self

        for point in wall.body:
            if x == point.x * BLOCK and y == point.y * BLOCK:
                running = False  # hit wall obstacle

        snake.append((x, y))
        if len(snake) > length:
            del snake[0]

        pygame.draw.rect(screen, (255, 0, 0), (*food, BLOCK, BLOCK))

        if (x, y) == food:
            food = generate_food(snake, wall)
            length += 1
            score += 1

            if score % 5 == 0:
                level = (level + 1) % MAX_LEVEL
                wall = Wall(level)
                food = generate_food(snake, wall)
                speed += 1

        draw_snake(snake)
        draw_score(score, level)
        pygame.display.update()
        clock.tick(speed)

    save_game_state(user_id, level, score)
    pygame.quit()

main()
connection.close()