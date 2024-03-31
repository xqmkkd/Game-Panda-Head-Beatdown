import sys
from time import sleep
import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event, ship):
	"""响应松开"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
				
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)
			
def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
	"""单击play开始游戏"""
	button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active:
		#重置速度
		ai_settings.initialize_dynamic_settings()
		#隐藏光标
		pygame.mouse.set_visible(False)
		#重置统计信息
		stats.reset_stats()
		stats.game_active = True
		#重置积分
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_ships()
		#清空外星人 子弹
		aliens.empty()
		bullets.empty()
		#重置外星人
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()

def update_screen(ai_settings,screen,stats,sb,ship,alien,bullets,play_button):
	"""更新屏幕"""
	screen.fill(ai_settings.bg_color)
	#重绘子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	alien.draw(screen)
	sb.show_score()
	if not stats.game_active:
		play_button.draw_botton()
	#绘制屏幕
	pygame.display.flip()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
	"""更新子弹位置 删除消失的子弹"""
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <=0:
			bullets.remove(bullet)
	check_bullet_alien_collision(ai_settings,screen,stats,sb,ship,aliens,bullets)
	
	

def check_bullet_alien_collision(ai_settings,screen,stats,sb,ship,aliens,bullets):
	"""碰撞"""
	collisions = pygame.sprite.groupcollide(bullets,aliens,False,True)
	if collisions:
		for aliens in collisions.values():
			#加分
			stats.score += ai_settings.alien_points
			sb.prep_score()
		#更新最高分
		check_high_score(stats,sb)
		
	if len(aliens) == 0:
		bullets.empty()
		#加难度
		ai_settings.increase_speed()
		#升级
		stats.level +=1
		sb.prep_level()
		#新一波外星人
		create_fleet(ai_settings,screen,ship,aliens)
		
def fire_bullet(ai_settings,screen,ship,bullets):
	"""发射子弹"""
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)

def get_number_aliens_x(ai_settings,alien_width):
	"""每行多少个外星人"""
	available_space_x = ai_settings.screen_width - 2* alien_width
	number_aliens_x = int(available_space_x / (2*alien_width))
	return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
	"""屏幕可容纳多少外星人"""
	available_space_y = (ai_settings.screen_height - (2*alien_height)-ship_height)
	number_rows = int(available_space_y/(2*alien_height))
	return number_rows
	
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	"""创建一个外星人放在当前行"""
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2*alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
	aliens.add(alien)
	
def create_fleet(ai_settings,screen,ship,aliens):
	"""创建外星人群"""
	#创建一个外星人，计算每行可以有多少个外星人
	alien = Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
	
	#创建第一行外星人
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number,row_number)

def check_fleet_edges(ai_settings,aliens):
	"""外星人到边缘 采取措施"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break
			
def change_fleet_direction(ai_settings,aliens):
	"""外星人下移"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets):
	"""飞船毁损"""
	if stats.ships_left >0:
		stats.ships_left -=1
		#更新飞船数量
		sb.prep_ships()
		#清空外星人和子弹
		aliens.empty()
		bullets.empty()
		#创建新外星人 飞船
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()
		#暂停
		sleep(0.5)
	else:
		stats.game_active =False
		pygame.mouse.set_visible(True)

def check_aliens_bottoms(ai_settings,stats,sb,screen,ship,aliens,bullets):
	"""外星人到达底部"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings,stats,sb,screen,ship,alien,bullets)
			break
			
def update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets):
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
	#检测外星人和飞船的碰撞
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
	#检查外星人到底部
	check_aliens_bottoms(ai_settings,stats,sb,screen,ship,aliens,bullets)

def check_high_score(stats,sb):
	"""更新最高分"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()
