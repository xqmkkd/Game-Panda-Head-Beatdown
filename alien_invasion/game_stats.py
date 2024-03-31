class GameStats():
	"""积分"""
	def __init__(self,ai_settings):
		"""初始化"""
		self.game_active = False
		self.ai_settings = ai_settings
		self.reset_stats()
		self.high_score = 0
		
	def reset_stats(self):
		"""变化积分"""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
