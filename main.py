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
	======================================
	Game Mechanics:
	======================================
	The game is similar to rock-paper-scissors. 
	Pick a weapon and see if you beat the opponent.
	The goal is to make the opponent's HP zero.

	-Sword wins against magic wand
	-Magic wand wins against shield
	-Shield wins agains sword

	======================================
	Controls:
	======================================
	Pick a weapon you will play by pressing the corresponding keys:
	[Q] for Sword
	[W] for Wand
	[E] for Shield

	If you have Magic points you can add an element to your weapon.
	[1] for Fire
	[2] for Water
	[3] for Wind
	[4] for Earth

	======================================
	Elememts:
	======================================
	Every turn you gain 1 Magic Point
	
	Fire gives additional damage. Costs 2 Magic Points
	Water heals the player Costs 2 Magic Points
	Wind deals massive damage gets reflected by Earth. Costs 3 Magic Points
	Earth reflects Wind element. Costs 2 Magic Points

'''

# global variables
p1_flag = True
p1_hp = 10
p1_mp = 0
p1_magic = False
p1_wp

p2_flag = False
p2_hp = 10
p2_mp = 0
p2_magic = False
p2_wp

# functions
def getWinner(p1_wp,p2_wp):
	if p1_wp == p2_wp:
		return 0 # tie



