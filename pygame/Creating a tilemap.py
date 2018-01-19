import pygame, sys
from pygame.locals import*

BLACK = (0, 0, 0 )
BROWN = (153, 76, 0 )
GREEN = (0, 255, 0 )
BLUE = (0, 0, 255)
RED = (255, 0, 0 )
GREY = (112, 138, 144)

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
LAVA = 4
ROCK = 5

colours = {
			DIRT : BROWN,
			GRASS : GREEN,
			WATER : BLUE,
			COAL : BLACK,
                        LAVA : RED,
                        ROCK : GREY
			}
			
tilemap = [
                 [GRASS, COAL, DIRT, DIRT, DIRT],
		 [WATER, WATER, GRASS, ROCK, LAVA],
		 [COAL, GRASS, WATER, LAVA, LAVA],
		 [DIRT, GRASS, COAL, ROCK, ROCK],
		 [GRASS, WATER, DIRT, WATER, LAVA],
                 [LAVA, ROCK, WATER, DIRT, COAL],
                 [LAVA, ROCK, LAVA, ROCK, LAVA]
                         
                        ]
                        
TILESIZE = 40
MAPWIDTH = 5
MAPHEIGHT = 5

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			pygame.draw.rect(DISPLAYSURF, colours[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
	
	pygame.display.update()
