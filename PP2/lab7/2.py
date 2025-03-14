import pygame
import os
pygame.init()

songs = ['Dance_monkey.mp3', 'Just_the_two_of_us.mp3', 'Lazy_song.mp3', 'Notion.mp3', 'Shape_of_you.mp3']
cur = 0
playing = False
def play_music():
    global playing
    pygame.mixer.music.load(songs[cur])
    pygame.mixer.music.play()
    playing = True

def play_next_song():
    global cur
    cur = (cur + 1) % len(songs)
    play_music()

def play_previous_song():
    global cur
    cur = (cur - 1) % len(songs)
    play_music()

def stop():
    global playing
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        playing = False
    else:
        pygame.mixer.music.unpause()
        playing = True

screen = pygame.display.set_mode((500, 200))
running = True
print("Music Player control buttons: Z - previous song, X - next song, Space - Pause / Unpause")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE: 
                if not playing:
                    play_music()
                else:
                    stop()
            elif event.key == pygame.K_x: 
                play_next_song()
            elif event.key == pygame.K_z: 
                play_previous_song()

    screen.fill("purple")
    pygame.display.flip()