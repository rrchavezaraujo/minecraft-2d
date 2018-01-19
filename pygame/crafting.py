import pygame, sys, random

from pygame.locals import *






BLACK = (0,0,0)
BROWN = (153,76,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREY = (112,138,144)
RED = (255,0,0)
LIGHTBLUE = (55,55,255)
WHITE = (255,255,255)  


cloudx = -200
cloudy = 0

birdx = -200
birdy = 100

mistcloudx = 200
mistcloudy = 200


DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
STONE = 4
LAVA = 5
DIAMOND = 6
CLOUD = 7
BIRD = 8
MISTCLOUD = 9
WOOD = 10
COBBLE = 11
GLASS = 12
BRICK = 13
SAND = 14
FIRE = 15




textures = {
			DIRT : pygame.image.load('H:/pygame/Minecraft.pngs/dirt.png'),
			GRASS : pygame.image.load('H:/pygame/Minecraft.pngs/grass.png'),
			WATER : pygame.image.load('H:/pygame/Minecraft.pngs/water.png'),
			COAL : pygame.image.load('H:/pygame/Minecraft.pngs/coal.png'),
			STONE : pygame.image.load('H:/pygame/Minecraft.pngs/stone.png'),
			LAVA : pygame.image.load('H:/pygame/Minecraft.pngs/lava.png'),
			DIAMOND : pygame.image.load('H:/pygame/Minecraft.pngs/diamond.png'),
			CLOUD : pygame.image.load('H:/pygame/Minecraft.pngs/cloud.png'),
			BIRD : pygame.image.load('H:/pygame/Minecraft.pngs/bird.png'),
			MISTCLOUD : pygame.image.load('H:/pygame/Minecraft.pngs/mistcloud.png'),
			WOOD : pygame.image.load('H:\pygame\Minecraft.pngs/wood.png'),
			COBBLE : pygame.image.load('H:\pygame\Minecraft.pngs/cobble.png'),
			FIRE : pygame.image.load('H:\pygame\Minecraft.pngs/fire.png'),
			GLASS : pygame.image.load('H:\pygame\Minecraft.pngs/glass.png'),
			BRICK : pygame.image.load('H:\pygame\Minecraft.pngs/brick.png'),
			SAND : pygame.image.load('H:\pygame\Minecraft.pngs/sand.png')
			}


inventory = {
			DIRT : 0,
			GRASS : 0,
			WATER : 0,
			COAL : 0,
			STONE : 0,
			LAVA : 0,
			DIAMOND : 0,
			WOOD :0,
			COBBLE :0,
			FIRE :0,
			GLASS :0,
			BRICK :0,
			SAND :0
			}
			

controls = {
    DIRT  : 49,     
    GRASS : 50,     
    WATER : 51,     
    COAL  : 52,     
    STONE  : 53,     
    LAVA  : 54,     
    DIAMOND : 55,     
    WOOD  : 56,     
    SAND  : 57    
     }
      


craft = {
		WOOD	: { STONE : 1, DIRT : 2},
		FIRE	: { WOOD : 2, STONE : 2},
		COBBLE	: { STONE : 2},
		GLASS	: { FIRE : 1, SAND : 2},
		BRICK	: { STONE : 2, FIRE : 1},
		SAND	: { STONE : 2}
		}			
	
	
	
TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20


PLAYER = pygame.image.load('H:/pygame/Minecraft.pngs/player.png')

playerPos = [0,0]


resources = [DIRT,GRASS,WATER,COAL,STONE,LAVA,DIAMOND,WOOD,FIRE,SAND,GLASS,COBBLE,BRICK]

tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]


pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE + 50))


INVFONT = pygame.font.Font('FreeSansBold.ttf', 18)

pygame.display.set_caption('M I N E C R F T -- 2 D')
pygame.display.set_icon(pygame.image.load('H:/pygame/Minecraft.pngs/player.png'))


for rw in range(MAPHEIGHT):
	
	for cl in range(MAPWIDTH):
		
		randomNumber = random.randint(0,15)
		
		if randomNumber == 0 or randomNumber == 1:
			tile = COAL
		elif randomNumber == 2 or randomNumber == 3:
			tile = WATER
		elif randomNumber == 4 or randomNumber == 5 or randomNumber == 6:
			tile = STONE
		elif randomNumber == 7 or randomNumber == 8 or randomNumber == 9 or randomNumber == 10:
			tile = GRASS
		elif randomNumber == 11 or randomNumber == 12:
			tile = LAVA
		elif randomNumber == 13 or randomNumber == 14:
			tile = DIRT
		elif randomNumber == 15:
			tile = DIAMOND
		
		tilemap[rw][cl] = tile
		



		
while True:

	fpsClock = pygame.time.Clock()
	
	DISPLAYSURF.fill(BLACK)	
		
	for event in pygame.event.get():
		print(event)
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
				
		
		elif event.type == KEYDOWN:
			if(event.key == K_RIGHT) and playerPos[0] < MAPWIDTH -1:
				playerPos[0] += 1
			if(event.key == K_LEFT) and playerPos[0] > 0:
				playerPos[0] -= 1
			if(event.key == K_UP) and playerPos[1] > 0:
				playerPos[1] -= 1
			if(event.key == K_DOWN) and playerPos[1] < MAPHEIGHT -1:
				playerPos[1] += 1
			if event.key == K_SPACE:
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				inventory[currentTile] += 1
				tilemap[playerPos[1]][playerPos[0]] = DIRT
			
			
			for key in controls:
				
				if (event.key == controls[key]):
					
					if pygame.mouse.get_pressed()[0]:
						
						if key in craft:
							
							canBeMade = True
						
						for i in craft[key]:
							if craft[key][i] > inventory[i]:
								
								canBeMade = False
								break
						
						if canBeMade == True:
							
							for i in craft[key]:
								inventory[i] -= craft[key][i]
							
							inventory[key] += 1
								
						
						else:
						
							
							currentTile = tilemap[playerPos[1]][playerPos[0]]
							
							if inventory[key] > 0:
								
								inventory[key] -= 1
								
								inventory[currentTile] += 1
								
								tilemap[playerPos[1]][playerPos[0]] = key
							
				
		
	
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
	
	DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))
	
	
	DISPLAYSURF.blit(textures[CLOUD].convert_alpha(),(cloudx,cloudy))
	
	cloudx+=2
	
	if cloudx > MAPWIDTH*TILESIZE:
		cloudy= random.randint(0,MAPHEIGHT*TILESIZE)
		cloudx = -200
		
	DISPLAYSURF.blit(textures[BIRD].convert_alpha(),(birdx,birdy))
	
	birdx+=6
	
	if birdx > MAPWIDTH*TILESIZE:
		birdy= random.randint(0,MAPHEIGHT*TILESIZE)
		birdx = -200
		
	DISPLAYSURF.blit(textures[MISTCLOUD].convert_alpha(),(mistcloudx,mistcloudy))
	
	mistcloudx-=3
	
	if mistcloudx < -200:
		mistcloudy= random.randint(0,MAPHEIGHT*TILESIZE)
		mistcloudx = MAPWIDTH*TILESIZE
		
	
	
	placePosition = 10
	for item in resources:
		DISPLAYSURF.blit(textures[item],(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition += 10
		textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
		DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition += 35
	
	pygame.display.update()
	fpsClock.tick(24)


