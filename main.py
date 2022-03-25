import pygame
import os
#import time
#import random
#pygame.font.init()
#pygame.mixer.init()

WIDTH, HEIGHT = 500, 500
SPRITE_WIDTH, SPRITE_HEIGHT = 25,25
HAIR_WIDTH, HAIR_HEIGHT = 50, 50
VEL = 5
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BORDER = pygame.Rect(0,0,WIDTH, HEIGHT)

pygame.display.set_caption('Snea Snakeroo0')

#CIRCLES = pygame.image.load(os.path.join('assets', 'circles.png'))
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'pot.png')), (WIDTH, HEIGHT))
MEATBALL = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'meatball.png')), (SPRITE_WIDTH, SPRITE_HEIGHT))
HAIR = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'hair.png')), (HAIR_WIDTH, HAIR_HEIGHT))

#RGB COLOR KEYS
BLACK = (0,0,0)
WHITE = (255,255,255)

#.set_colorkey makes these backgrounds transparent
HAIR.set_colorkey(WHITE)
MEATBALL.set_colorkey(WHITE)

#Vince staples loves this because it moves the sprite
def sprite_handle_movement(keys_pressed, sprite):
	if keys_pressed[pygame.K_a] and sprite.x - VEL > 0: #LEFT
		sprite.x -= VEL	
	if keys_pressed[pygame.K_d] and sprite.x + VEL + sprite.width < WIDTH: #RIGHT
		sprite.x += VEL	
	if keys_pressed[pygame.K_w] and sprite.y - VEL > 0: #UP
		sprite.y -= VEL	
	if keys_pressed[pygame.K_s] and sprite.y + VEL + sprite.height < HEIGHT: #DOWN
		sprite.y += VEL	

#window function
def draw_window(sprite):
	pygame.draw.rect(WIN,BLACK,BORDER)
	WIN.blit(BACKGROUND, (0,0))
	#WIN.blit(CIRCLES,(WIDTH - CIRCLES.get_width() + 50,0))
	WIN.blit(MEATBALL, (sprite.x, sprite.y))
	WIN.blit(HAIR, (200,200))
#main function loop
def main():	
	
	sprite = pygame.Rect(300,300, SPRITE_WIDTH, SPRITE_HEIGHT)

	FPS = 60
	clock = pygame.time.Clock()
	run = True

	while run:
		
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys_pressed = pygame.key.get_pressed()
		sprite_handle_movement(keys_pressed, sprite)
		draw_window(sprite)
		pygame.display.update()

if __name__ == "__main__":
	main()