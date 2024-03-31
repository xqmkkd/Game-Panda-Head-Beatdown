class Settings():
	def __init__(self):
		"""初始化游戏设置"""
		#屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		#飞船设置
		
		self.ship_limit = 2
		#子弹设置
		
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullets_allowed = 50
		#外星人设置
			#下落速度设置很大，将导致empty发生错误
		self.fleet_drop_speed = 10
		self.fleet_direction = 1
		#加大游戏难度
		self.speedup_scale = 1.1
		#加大奖励力度
		self.score_scale = 1.5
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		self.alien_points = 50
		
	def increase_speed(self):
		self.ship_speed_factor *=self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		
		self.alien_points = int(self.alien_points * self.score_scale)
		
