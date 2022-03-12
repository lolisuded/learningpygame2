import pygame
from sys import exit

pygame.init()

screen_dimensions = (800, 400)
screen = pygame.display.set_mode(screen_dimensions)

pygame.display.set_caption('POG')
clock = pygame.time.Clock()
game_active = True
start_time = 0

global_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_background = pygame.image.load('graphics/Sky.png').convert()
ground_background = pygame.image.load('graphics/ground.png').convert()

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0


def currentscore():
    current_time = pygame.time.get_ticks() - start_time
    score_text = global_font.render(f'{current_time}', False, (64, 64, 64))
    score_text_rect = score_text.get_rect(midtop=(400, 40))
    screen.blit(score_text, score_text_rect)


def movingRect(rect, direction, amount):
    if direction == "right":
        rect.right += amount
    elif direction == "left":
        rect.left -= amount


def keeprectonscreen(rect, offscreenxpos, resetxpos, direction):
    if direction == "left":
        if rect.right < offscreenxpos: rect.left = resetxpos
    if direction == "right":
        if rect.left > offscreenxpos: rect.left = resetxpos


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # elif event.type == pygame.MOUSEMOTION:
        #    mousepos = event.pos
        #    if player_rect.collidepoint(mousepos):
        #        print("AAAAA")
        if game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and player_rect.bottom == 300:
                player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.x = 600
                start_time = pygame.time.get_ticks()

    if game_active:

        screen.blit(sky_background, (0, 0))
        screen.blit(ground_background, (0, 300))

        movingRect(snail_rect, "left", 5)
        keeprectonscreen(snail_rect, 0, 800, "left")
        screen.blit(snail_surface, snail_rect)

        currentscore()

        player_gravity += 1
        player_rect[1] = player_rect[1] + player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        if snail_rect.colliderect(player_rect):
            game_active = False

    else:
        screen.fill("Yellow")

    pygame.display.update()
    clock.tick(60)
