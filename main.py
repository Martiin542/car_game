import pygame, random
from basic_variables import *
from cars import generate_car, move_cars
from functions import draw_hearts, explode_effect, draw_text
from label_button import label, button
from score import save_max_score

pygame.init()

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if main_menu == True: #menu principal
        screen.blit(background_image, (0, 0))
        play_button = button(screen, 30,350, 'assets\\buttons\\button_play.png', 1)
        exit_buton_mm = button(screen, 270,350, 'assets\\buttons\\button_exit.png', 1)
        if play_button:
            main_menu = False
        if exit_buton_mm:
            run = False
    elif game_paused == True: #pausa in game
        screen.fill('Yellow')
        draw_text(screen, 'Game Paused', font_game_over, TEXT_COL, 110,40)
        back_button = button(screen, 30,350, 'assets\\buttons\\button_back.png', 1)
        stop_song = button(screen, 270,350, 'assets\\buttons\\button_muete.png', 1)
        if back_button:
            game_paused = False
        if stop_song:
            mute_song = not mute_song
    elif game_over == True: #pantalla de game over
        screen.fill('Red')
        label(screen, 135,0, 'assets\\game_over.png', 1)
        draw_text(screen, f'Final Score: {score}', font_game_over, TEXT_COL, 0,0)
        replay_button = button(screen, 30,350, 'assets\\buttons\\button_replay.png', 1)
        exit_button_go = button(screen, 270,350, 'assets\\buttons\\button_exit.png', 1)
        if exit_button_go:
            run = False
        if replay_button:
            score = 0 
            game_over = False
            lives = 3
            

        if score > max_score:
            max_score = score
            save_max_score(max_score)
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
        
        if keys[pygame.K_ESCAPE]:
            game_paused = True
        
        #music
        song.play()
        if mute_song:
            pygame.mixer.pause()
        else:
            pygame.mixer.unpause()
        
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
        
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - score_timer) / 1000 

        if elapsed_time >= 4:
            score += 10
            score_timer = current_time

        draw_text(screen, f'Score: {score}', font_score, TEXT_COL, 5, 35)
        draw_text(screen, f'Max Score: {max_score}', font_score, TEXT_COL, 5, 60)

        last_spawn_time = generate_car(cars, car_images, last_spawn_time)
        lives = move_cars(cars, lives) 

        for car in cars:
            screen.blit(car[0], car[1])

    pygame.display.update()

pygame.quit()