import pygame
import sys
import random


pygame.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 800, 0)
RED = (800, 0, 0)
YELLOW = (255,255,0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 10
SNAKE_SPEED = 15


clock = pygame.time.Clock()


font_style = pygame.font.SysFont("bahnschrift", 25)




class Snake:
   def __init__(self):
       self.length = 1
       self.body = [[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]]
       self.direction = pygame.K_RIGHT


   def move(self):
       head_x, head_y = self.body[-1]


       if self.direction == pygame.K_LEFT:
           head_x -= BLOCK_SIZE
       elif self.direction == pygame.K_RIGHT:
           head_x += BLOCK_SIZE
       elif self.direction == pygame.K_UP:
           head_y -= BLOCK_SIZE
       elif self.direction == pygame.K_DOWN:
           head_y += BLOCK_SIZE


       self.body.append([head_x, head_y])


       if len(self.body) > self.length:
           del self.body[0]


   def change_direction(self, key):
       if key == pygame.K_LEFT and self.direction != pygame.K_RIGHT:
           self.direction = key
       elif key == pygame.K_RIGHT and self.direction != pygame.K_LEFT:
           self.direction = key
       elif key == pygame.K_UP and self.direction != pygame.K_DOWN:
           self.direction = key
       elif key == pygame.K_DOWN and self.direction != pygame.K_UP:
           self.direction = key


   def grow(self):
       self.length += 80


   def draw(self, screen):
       for segment in self.body:
           pygame.draw.rect(screen, GREEN, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])


   def check_collision(self):
       head_x, head_y = self.body[-1]
       if head_x >= SCREEN_WIDTH or head_x < 0 or head_y >= SCREEN_HEIGHT or head_y < 0:
           return True


       if self.body[-1] in self.body[:-1]:
           return True


       return False




class Food:
   def __init__(self):
       self.x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
       self.y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0


   def reposition(self):
       self.x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
       self.y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0


   def draw(self, screen):
       pygame.draw.rect(screen, RED, [self.x, self.y, BLOCK_SIZE, BLOCK_SIZE])




class Game:
   def __init__(self):
       self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
       pygame.display.set_caption('Snake Game')
       self.snake = Snake()
       self.food = Food()


   def display_message(self, msg, color):
       mesg = font_style.render(msg, True, color)
       self.screen.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])


   def game_loop(self):
       game_over = False
       game_close = False


       while not game_over:


           while game_close:
               self.screen.fill(BLACK)
               self.display_message("Game Over! Press Q-Quit or C-Play Again", RED)
               pygame.display.update()


               for event in pygame.event.get():
                   if event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_q:
                           game_over = True
                           game_close = False
                       if event.key == pygame.K_c:
                           self.__init__()
                           self.game_loop()


           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   game_over = True
               if event.type == pygame.KEYDOWN:
                   self.snake.change_direction(event.key)


           self.snake.move()


           if self.snake.check_collision():
               game_close = True


           self.screen.fill(BLACK)
           self.food.draw(self.screen)
           self.snake.draw(self.screen)
           pygame.display.update()


           if self.snake.body[-1][0] == self.food.x and self.snake.body[-1][1] == self.food.y:
               self.food.reposition()
               self.snake.grow()


           clock.tick(SNAKE_SPEED)


       pygame.quit()
       sys.exit()




if __name__ == "__main__":
   game = Game()
   game.game_loop()



