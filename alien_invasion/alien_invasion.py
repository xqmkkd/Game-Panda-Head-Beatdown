import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship

import game_functions as gf

def run_game():
	#初始化游戏，创建一个对象
	pygame.init()
	ai_settings = Settings()
	#设置宽高
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	#创建play按钮
	play_button = Button(ai_settings,screen,"Play")
	
	#积分
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	#创建飞船
	ship=Ship(ai_settings,screen)
	#创建子弹编组
	bullets = Group()
	#创建一群外星人
	aliens = Group()
	gf.create_fleet(ai_settings,screen,ship,aliens)
	# 开始游戏的主循环
	while True:
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()

