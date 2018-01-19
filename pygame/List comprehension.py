import pygame, sys, random
from pygame.locals import*

BLACK = (0, 0, 0 )
BROWN = (153, 76, 0 )
GREEN = (0, 255, 0 )
BLUE = (0, 0, 255)

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
LAVA = 4
ROCK = 5
DIAMOND = 6

textures = {
			DIRT : pygame.image.load('dirt.png'),
			GRASS : pygame.image.load('grass.png'),
			WATER : pygame.image.load('water.png'),
			COAL : pygame.image.load('coal.png'),
                        LAVA : pygame.image.load('lava.png'),
                        ROCK : pygame.image.load('rock.png'),
                        DIAMOND : pygame.image.load('diamond.png')

			}
			
tilemap = [
                [GRASS, COAL, DIRT, ROCK, LAVA],
				[WATER, WATER, GRASS, LAVA, ROCK],
				[COAL, GRASS, WATER, LAVA, LAVA],
				[DIRT, GRASS, COAL, LAVA, WATER],
				[GRASS, WATER, DIRT, ROCK, ROCK],
                                [WATER, WATER, DIAMOND, WATER, WATER]
                        ]
                        
TILESIZE = 40
MAPWIDTH = 30
MAPHEIGHT = 50
resources = [DIRT,GRASS,WATER,COAL,LAVA,ROCK,DIAMOND]

tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT) ]

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
for rw in range(MAPHEIGHT):
        for cl in range(MAPWIDTH):
                randomNumber = random.randint(0,15)
                if randomNumber == 0 or randomNumber == 1:
                        tile = COAL
                elif randomNumber == 2 or randomNumber == 3:
                        tile = WATER
                elif randomNumber == 4 or randomNumber == 5:
                        tile = GRASS
                elif randomNumber == 6 or randomNumber == 7:
                        tile = LAVA
                elif randomNumber == 8 or randomNumber == 9:
                        tile = ROCK
                elif randomNumber == 10:
                        tile = DIAMOND
                else:
                         tile = DIRT
                tilemap[rw][cl] = tile
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
	
	pygame.display.update()
