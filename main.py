import pygame, random
from basic_variables import *
from cars import generate_car, move_cars
from functions import draw_hearts, explode_effect

pygame.init()

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if main_menu == True: #menu principal
        pass
    elif game_paused == True: #pausa in game
        pass
    elif game_over == True: #pantalla de game over
        screen.fill('Red')
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and  player_rect.left > left_lateral_lines[0] + marker_width:
            player_rect.left -= speed
        if keys[pygame.K_RIGHT] and player_rect.right < right_lateral_lines[0] - marker_width:
            player_rect.right += speed
        if keys[pygame.K_UP] and player_rect.top > 0:
            player_rect.top -= speed
        if keys[pygame.K_DOWN] and player_rect.bottom < SCREEN_H:
            player_rect.bottom += speed
        
        #pasto
        screen.fill('Green')
        #road
        pygame.draw.rect(screen, 'Gray', road)
        #lateral lines
        pygame.draw.rect(screen, 'Yellow', left_lateral_lines)
        pygame.draw.rect(screen, 'Yellow', right_lateral_lines)
        #lane
        lane_move_y += speed * 2
        if lane_move_y >= marker_height * 2:
            lane_move_y = 0
        for i in range(marker_height * -2, SCREEN_H, marker_height * 2):
            pygame.draw.rect(screen, 'White', (left_lane + 45, i + lane_move_y, marker_width, marker_height))
            pygame.draw.rect(screen, 'White', (center_lane + 45, i + lane_move_y, marker_width, marker_height))
        
        screen.blit(scaled_img, player_rect.topleft)

        draw_hearts(screen, lives)
        if lives <= 0:
            game_over = True
            explode_effect(player_rect)


        last_spawn_time = generate_car(cars, car_images, last_spawn_time)
        lives = move_cars(cars, lives) 

        for car in cars:
            screen.blit(car[0], car[1])

    pygame.display.update()

pygame.quit()