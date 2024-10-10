# # # Example file showing a basic pygame "game loop"
# # import pygame

# # # pygame setup
# # pygame.init()
# # screen = pygame.display.set_mode((1280, 720))
# # clock = pygame.time.Clock()
# # running = True

# # while running:
# #     # poll for events
# #     # pygame.QUIT event means the user clicked X to close your window
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False

# #     # fill the screen with a color to wipe away anything from last frame
# #     screen.fill("blue")

# #     # RENDER YOUR GAME HERE

# #     # flip() the display to put your work on screen
# #     pygame.display.flip()

# #     clock.tick(60)  # limits FPS to 60

# # pygame.quit()

# # Example file showing a circle moving on screen
# import pygame

# # pygame setup
# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# clock = pygame.time.Clock()
# running = True
# dt = 0

# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# while running:
#     # poll for events
#     # pygame.QUIT event means the user clicked X to close your window
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # fill the screen with a color to wipe away anything from last frame
#     screen.fill("yellow")

#     pygame.draw.circle(screen, "red", player_pos, 120)

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_w]:
#         player_pos.y -= 300 * dt
#     if keys[pygame.K_s]:
#         player_pos.y += 300 * dt
#     if keys[pygame.K_a]:
#         player_pos.x -= 300 * dt
#     if keys[pygame.K_d]:
#         player_pos.x += 300 * dt

#     # flip() the display to put your work on screen
#     pygame.display.flip()

#     # limits FPS to 80
#     # dt is delta time in seconds since last frame, used for framerate-
#     # independent physics.
#     dt = clock.tick(60) / 1000

# pygame.quit()


import pygame
import sys
import random


pygame.init()


screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
Yellow = (255,255,0)

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 7


snake_list = []
snake_length = 1


font_style = pygame.font.SysFont("bahnschrift", 25)


def our_snake(snake_block, snake_list):
   for x in snake_list:
       pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
   mesg = font_style.render(msg, True, color)
   screen.blit(mesg, [screen_width / 6, screen_height / 3])


def game_loop():
   game_over = False
   game_close = False


   x1 = screen_width / 2
   y1 = screen_height / 2


   x1_change = 0
   y1_change = 0


   global snake_list
   snake_list = []
   global snake_length
   snake_length = 1


   food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
   food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0


   while not game_over:


       while game_close == True:
           screen.fill(BLACK)
           message("Game Over! Press Q-Quit or C-Play Again", YELLOW)
           pygame.display.update()


           for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_q:
                       game_over = True
                       game_close = False
                   if event.key == pygame.K_c:
                       game_loop()


       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               game_over = True
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                   x1_change = -snake_block
                   y1_change = 0
               elif event.key == pygame.K_RIGHT:
                   x1_change = snake_block
                   y1_change = 0
               elif event.key == pygame.K_UP:
                   y1_change = -snake_block
                   x1_change = 0
               elif event.key == pygame.K_DOWN:
                   y1_change = snake_block
                   x1_change = 0


       if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
           game_close = True


       x1 += x1_change
       y1 += y1_change
       screen.fill(BLACK)


       pygame.draw.rect(screen, RED, [food_x, food_y, snake_block, snake_block])


       snake_head = []
       snake_head.append(x1)
       snake_head.append(y1)
       snake_list.append(snake_head)
       if len(snake_list) > snake_length:
           del snake_list[0]


       for x in snake_list[:-1]:
           if x == snake_head:
               game_close = True


       our_snake(snake_block, snake_list)


       pygame.display.update()


       if x1 == food_x and y1 == food_y:
           food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
           food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
           snake_length += 1


       clock.tick(snake_speed)


   pygame.quit()
   sys.exit()


game_loop()
