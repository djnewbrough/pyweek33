import pygame
import os
#import time
#import random
#pygame.font.init()
#pygame.mixer.init()

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BORDER = pygame.Rect(0,0,WIDTH, HEIGHT)
pygame.display.set_caption('Snea Snakeroo0')
CIRCLES = pygame.image.load(os.path.join('assets', 'circles.png'))
BG = pygame.image.load(os.path.join('assets', 'mountains.png'))
BLACK = (0,0,0)
#create window

def draw_window():
	pygame.draw.rect(WIN,BLACK,BORDER)
	WIN.blit(BG, (0,0))
	WIN.blit(CIRCLES,(300,300))

def main():
	
	run = True

	while run:
		draw_window()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		pygame.display.update()
main()

if __name__ == "__main__":
	main()