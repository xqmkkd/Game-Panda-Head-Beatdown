import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self,ai_settings,screen):
		"""初始化飞船 设置初始位置"""
		super(Ship,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		#获取飞船外接矩形
		self.image = pygame.image.load("images/panda.jpg")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		#飞船放在底部
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		self.center = float(self.rect.centerx)
		#飞船移动状态
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left>0:
			self.center -= self.ai_settings.ship_speed_factor
		
		self.rect.centerx = self.center
	def blitme(self):
		"""指定位置绘制飞船"""
		self.screen.blit(self.image,self.rect)
	
	def center_ship(self):
		self.center = self.screen_rect.centerx
