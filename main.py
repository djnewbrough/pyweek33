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

BLACK = (0,0,0)
#create window

def draw_window():
	pygame.draw.rect(WIN,BLACK,BORDER)
	
def main():
	

	run = True

	while run:
		draw_window()

main()

if __name__ == "__main__":
	main()