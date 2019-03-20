import pygame

BLACK = (0,0,0)
RED=  (225,0,225)

class Rectangle(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image=pygame.Surface([200,200])
		self.image.fill(RED)
		self.rect=self.image.get_rect()


	def update(self):
		positionMouse= pygame.mouse.get_pos()
		self.rect.x=positionMouse[0]
		self.rect.y=positionMouse[1]



pygame.init()
screen = pygame.display.set_mode([800,800])
test = False
rectangle1=Rectangle()
while not test:
	for event in pygame.event.get():
		if event.type== pygame.QUIT:
			test=True

	screen.fill(BLACK)
	rectangle1.update()
	pygame.draw.rect(screen,RED,rectangle1,0)

	pygame.display.flip()
pygame.quit()
