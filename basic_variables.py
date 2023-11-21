import pygame

pygame.init()
pygame.mixer.init()

#variables basicas
FPS = 60
clock = pygame.time.Clock()
SCREEN_W = 500
SCREEN_H = 500
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
timer = pygame.time.Clock()

#estados del juego
main_menu = False
game_paused = False
game_over = False

#Road
road = (100, 0, 300, SCREEN_H)

#lines
marker_width = 10
marker_height = 40

#lateral lines
left_lateral_lines = (95, 0, marker_width, SCREEN_H)
right_lateral_lines = (395, 0, marker_width, SCREEN_H)

#lane (carriles)
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]
lane_move_y = 0

#player
speed = 4
car_image = pygame.image.load('assets\\car.png')
width, heigth = car_image.get_size()
new_width = int(width * 0.6)
new_height = int(heigth * 0.6)
scaled_img = pygame.transform.scale(car_image, (new_width, new_height))
player_rect = scaled_img.get_rect()
player_rect.topleft = (230, 400)
score = 0
score_timer = 0

#enmeys
car_images = [
    pygame.image.load('assets\\pickup_truck.png'),
    pygame.image.load('assets\\pickup_truck.png'),
    pygame.image.load('assets\\semi_trailer.png'),
    pygame.image.load('assets\\taxi.png'),
    pygame.image.load('assets\\van.png')
]
cars = []
last_spawn_time = pygame.time.get_ticks()

#vidas
lives = 3  
heart_image = pygame.image.load('assets\\corazon.png')
heart_width, heart_height = 30, 30
heart_image = pygame.transform.scale(heart_image, (heart_width, heart_height))
collision_sound = pygame.mixer.Sound('assets\\sound_crash.mp3')
collision_sound.set_volume(0.5) 

#explosion
explosion_image = pygame.image.load('assets\\crash.png')
explosion_width, explosion_height = 100, 100
explosion_image = pygame.transform.scale(explosion_image, (explosion_width, explosion_height))
explosion_sound = pygame.mixer.Sound('assets\\sound_explosion.mp3')
explosion_sound.set_volume(0.5)


