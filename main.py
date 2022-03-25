import pygame
import os
#import time
#import random
#pygame.font.init()
#pygame.mixer.init()

WIDTH, HEIGHT = 1250, 600
SPRITE_WIDTH, SPRITE_HEIGHT = 25,25
HAIR_WIDTH, HAIR_HEIGHT = 50, 50
POT_WIDTH, POT_HEIGHT = 250, 100
STOVE_WIDTH, STOVE_HEIGHT = 800, 140

VEL = 5
MEATBALL_VEL = 10
HAIRNET_VEL = 15

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BORDER = pygame.Rect(0,0,WIDTH, HEIGHT)

pygame.display.set_caption('Snea Snakeroo0')

POT = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'pot.png')), (POT_WIDTH, POT_HEIGHT))
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'kitchen.png')), (WIDTH, HEIGHT))
MEATBALL = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'meatball.png')), (SPRITE_WIDTH, SPRITE_HEIGHT))
HAIR = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'hair.png')), (HAIR_WIDTH, HAIR_HEIGHT))
STOVE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'stove.png')),(STOVE_WIDTH, STOVE_HEIGHT))


#RGB COLOR KEYS
BLACK = (0,0,0)
WHITE = (255,255,255)

#.set_colorkey makes these backgrounds transparent
HAIR.set_colorkey(WHITE)
MEATBALL.set_colorkey(WHITE)
POT.set_colorkey(WHITE)

#Vince staples loves this because it moves the sprite
def pot_handle_movement(keys_pressed, pot_sprite):
	if keys_pressed[pygame.K_a] and pot_sprite.x - VEL > 0: #LEFT
		pot_sprite.x -= VEL	
	if keys_pressed[pygame.K_d] and pot_sprite.x + VEL + pot_sprite.width < WIDTH: #RIGHT
		pot_sprite.x += VEL	
	

#window function
def draw_window(sprite, pot_sprite):
	pygame.draw.rect(WIN,BLACK,BORDER)
	WIN.blit(BACKGROUND, (0,0))
	#WIN.blit(CIRCLES,(WIDTH - CIRCLES.get_width() + 50,0))
	WIN.blit(MEATBALL, (sprite.x, sprite.y))
	WIN.blit(HAIR, (200,200))
	WIN.blit(POT, (pot_sprite.x, pot_sprite.y))
	WIN.blit(STOVE, ((WIDTH/2 - STOVE_WIDTH/2), (HEIGHT - STOVE_HEIGHT)))
#main function loop
def main():	
	
	sprite = pygame.Rect(300,300, SPRITE_WIDTH, SPRITE_HEIGHT)
	pot_sprite = pygame.Rect((WIDTH/2 - POT_WIDTH/2), (HEIGHT - STOVE_HEIGHT- POT_HEIGHT), POT_WIDTH, POT_HEIGHT)


	FPS = 60
	clock = pygame.time.Clock()
	run = True

	while run:
		
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys_pressed = pygame.key.get_pressed()
		pot_handle_movement(keys_pressed, pot_sprite)
		draw_window(sprite, pot_sprite)
		pygame.display.update()

if __name__ == "__main__":
	main()