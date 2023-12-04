import pygame


class Explosao(pygame.sprite.Sprite):
	def __init__(self, x, y, sprites):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		for num in range(len(sprites)):
			img = pygame.image.load(sprites[num])
			img = pygame.transform.scale(img, (80, 80))
			self.images.append(img)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.counter = 0

	def update(self):
		
		explosion_speed = 4
		#update explosion animation
		self.counter += 1

		if self.counter >= explosion_speed and self.index < len(self.images) - 1:
			self.counter = 0
			self.index += 1
			self.image = self.images[self.index]

		#if the animation is complete, reset animation index
		if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
			self.kill()