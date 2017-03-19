# from pygame.locals import *

# import os
# import pygame
# import sys

# pygame.init()
# pygame.display.set_caption('Tic Tac Toe')

# set up the window
# windowSurface = pygame.display.set_mode((1024, 600))
# mainClock = pygame.time.Clock()
# os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (25,50) # set initial screen position
# bg  = pygame.image.load('res/img/bg2.png').convert_alpha()

# while True:
# 	# load bg
# 	windowSurface.blit(bg,(0,0))
# 	for event in pygame.event.get():
# 		if event.type==pygame.QUIT:
# 			# if it is quit the game
# 			pygame.quit()
# 			exit(0)
# 	pygame.display.update()
# 	mainClock.tick(30)

print '''
	How to Play:
	======================================
	Pick a weapon you will play by pressing the corresponding keys:
	[Q] for Sword
	[W] for Wand
	[E] for Shield

	If you have Magic point you can add an element to your weapon.
	[1] for Fire
	[2]	for Water
	[3]	for Wind
	[4] for Earth
	Rules:
	======================================
	sword wins against magic wand
	magic wand wins against shield
	shield wins agains sword
	======================================
	Elememts
	Every turn you gain 1 Magic Point
	
	Fire gives additional damage. Costs 2 Magic Point
	Water heals the player Costs 2 Magic Point
	Wind deals massive damage gets reflected by Earth. Costs 3 Magic Point
	Earth reflects Wind element. Costs 2 Magic Point

'''