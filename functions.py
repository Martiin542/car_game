import pygame, json, time
from basic_variables import *

def draw_hearts(screen, lives):
    heart_spacing = 40
    for i in range(lives):
        screen.blit(heart_image, (10 + i * heart_spacing, 10))

def explode_effect(player_rect):
    explosion_rect = explosion_image.get_rect(center = player_rect.center)
    screen.blit(explosion_image, explosion_rect.topleft)
    pygame.display.update()
    pygame.time.delay(1000) 
    explosion_sound.play()

def draw_text(screen, text, font, text_col, x, y):
    """
    Dibuja texto en una superficie de pantalla con la fuente y color especificados.
    Parámetros:
    - screen (pygame.Surface): La superficie de pantalla en la que se dibujará el texto.
    - text (str): El texto que se desea mostrar en la pantalla.
    - font (pygame.font.Font): La fuente que se utilizará para renderizar el texto.
    - text_col (tuple): El color del texto representado como una tupla (R, G, B) o (R, G, B, A).
    - x (int): La coordenada x en la que se dibujará el texto en la superficie de pantalla.
    - y (int): La coordenada y en la que se dibujará el texto en la superficie de pantalla.

    Retorna:
    Ninguno (None)

    Esta función renderiza el texto en la fuente especificada y lo coloca en la posición (x, y)
    en la superficie de pantalla, utilizando el color de texto proporcionado.
    """
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))