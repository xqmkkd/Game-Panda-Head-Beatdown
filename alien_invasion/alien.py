import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""表示单个外星人"""
	def __init__(self,ai_settings,screen):
		super(Alien,self).__init__()
		self.screen = screen
		self.ai_settings =ai_settings
		
		self.image = pygame.image.load('images/alien.jpg')
		self.rect = self.image.get_rect()
		
		self.rect.x = 0
		self.rect.y = 0
		
		self.x=float(self.rect.x)
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def check_edges(self):
		"""外星人碰到边缘"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >=screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
			
	def update(self):
		"""向右移动外星人"""
		self.x += (self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
		self.rect.x = self.x
