import pygame, random
from basic_variables import *

def generate_car(car_list, img_path, last_spawn_time):
    current_time = pygame.time.get_ticks()

    if current_time - last_spawn_time > random.randint(2000, 4000):
        lane = random.choice(lanes)
        car_image = random.choice(img_path)
        width, height = car_image.get_size()
        new_width = int(width * 0.55)
        new_height = int(height * 0.55)
        scaled_img = pygame.transform.scale(car_image, (new_width, new_height))
        car_rect = scaled_img.get_rect()

        if lane == left_lane:
            car_rect.topleft = (left_lane - 25, -new_height)
        elif lane == center_lane:
            car_rect.topleft = (center_lane - 25 , -new_height) 
        elif lane == right_lane:
            car_rect.topleft = (right_lane - 25, -new_height) 
        car_speed = random.uniform(4, 10)
        car_list.append((scaled_img, car_rect, car_speed))
        return current_time
    
    return last_spawn_time

    

def move_cars(car_list, lives):

    for car in car_list[:]:
        car[1].y += car[2]

        if car[1].top > SCREEN_H:
            car_list.remove(car)
        elif car[1].colliderect(player_rect):
            car_list.remove(car)
            lives -= 1
            collision_sound.play()
    return lives
