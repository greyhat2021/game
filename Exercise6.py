import pygame
import time

pygame.init()

window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption('Simple Image Rendering with Slow Animation')

image = pygame.image.load('virat.jpg')

image_rect = image.get_rect()

image_rect.topleft = (0, 0)

background_color = (255, 255, 255)

speed_x = 1
speed_y = 1

loop_duration = 5

start_time = time.time()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if time.time() - start_time >= loop_duration:
        running = False

    image_rect.x += speed_x
    image_rect.y += speed_y

    if image_rect.right >= window_width or image_rect.left <= 0:
        speed_x = -speed_x
    if image_rect.bottom >= window_height or image_rect.top <= 0:
        speed_y = -speed_y

    window.fill(background_color)
    window.blit(image, image_rect)

    pygame.display.update()
pygame.quit()
