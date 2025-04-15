import pygame
import os
import time

pygame.init()

_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path).convert_alpha()
        _image_library[path] = image
    return image

def rot_center(image, angle, center):
    rotated_image = pygame.transform.rotate(image, -angle) 
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect

screen = pygame.display.set_mode((800, 600))
running = True
clock = pygame.time.Clock()

clock_face = get_image("clock.png")
minute_hand = get_image("min_hand.png") 
second_hand = get_image("sec_hand.png") 

clock_rect = clock_face.get_rect(center=(400, 300)) 
center = clock_rect.center

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    min_angle = (minutes % 60) * 6 
    sec_angle = (seconds % 60) * 6 

    rotated_minute, min_rect = rot_center(minute_hand, min_angle, center)
    rotated_second, sec_rect = rot_center(second_hand, sec_angle, center)

    screen.fill("White")
    screen.blit(clock_face, clock_rect.topleft) 
    screen.blit(rotated_minute, min_rect.topleft) 
    screen.blit(rotated_second, sec_rect.topleft) 

    pygame.display.flip()
    clock.tick(120) 