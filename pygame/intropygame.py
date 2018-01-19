import pygame, sys
from pygame.locals import*
pygame.init()
DISPLAYSURF = pygame.display.set_mode((300,300))
pygame.display.set_caption('My First Game')
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		pygame.draw.rect(DISPLAYSURF, (0,255,0), (100,50,40,50))
		pygame.draw.rect(DISPLAYSURF, (100,0,200), (120,50,20,20))
		pygame.draw.rect(DISPLAYSURF, (0,0,255), (190,50,60,90))
		pygame.draw.rect(DISPLAYSURF, (255,0,0), (10,50,80,10))
		pygame.draw.circle(DISPLAYSURF, (0,0,255), (150, 100), 25,25)
		pygame.draw.circle(DISPLAYSURF, (0,0,255), (350, 100),1)
		pygame.draw.line(DISPLAYSURF, (255,255,255),(60, 120), (120, 120), 1)
		pygame.draw.line(DISPLAYSURF, (255,255,255),(60, 120),(200, 356), 1)
		pygame.draw.arc(DISPLAYSURF, (0,150,0),(200,10,150,100), 0, 20)
		pygame.display.update()
