import pygame
import random
import sys

pygame.init()

width = 900
height = 600
player_color = (255, 255, 255)  # define as tuple
enemy_color = (215, 135, 143)
yellow = (255,255,0)
Bg_color = (114, 135, 143)
player_size = 20
enemy_size = 50
enemy_pos = [random.randint(0, width-enemy_size), 0]
enemy_list = [enemy_pos]
speed = 10
player_pos = [width/2, height - 2*player_size]  # define as list and let player on the bottom of the screen

score = 0



screen = pygame.display.set_mode((width, height))
game_over = False

clock = pygame.time.Clock()
myfont = pygame.font.SysFont("monospace", 25)
def set_level(score, speed):
    if score < 20:
        speed = 5
    elif score < 40:
        speed = 10
    elif score < 60:
        speed = 15
    else:
        speed = 20
    return speed
def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 15 and delay < 0.3:
        x_pos =random.randint(0, width-enemy_size)
        y_pos =0
        enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, enemy_color, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_enemy_positions(enemy_list, score):
    # update the position of enemy
    for idx, enemy_pos in enumerate(enemy_list):
      if enemy_pos[1] >= 0 and enemy_pos[1] < height:
         enemy_pos[1] += speed
      else:
          enemy_list.pop(idx)
          score += 1
    return(score)
def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos,player_pos):
            return True
    return False



def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    if ((p_x + player_size) > e_x and e_x >= p_x) or (p_x >= e_x and p_x < (e_x +enemy_size)):
        if (e_y >= p_y and e_y <(p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
              return True
    return False
while not game_over:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x -= 40
            elif event.key == pygame.K_RIGHT:
                x += 40
            player_pos = [x, y]

    screen.fill(Bg_color)

    if detect_collision(player_pos, enemy_pos):
        game_over = True
    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)
    speed = set_level(score, speed)
    text = "Score:" + str(score)
    label = myfont.render(text, 1, yellow)
    screen.blit(label, (width-175, height-40))

    if collision_check(enemy_list, player_pos):
        game_over = True


    draw_enemies(enemy_list)
    pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size, player_size))
    clock.tick(30)
    pygame.display.update()
