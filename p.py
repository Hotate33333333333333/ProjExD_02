import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1600, 900
KK_WIDTH, KK_HEIGHT = 100, 100
BOMB_RADIUS = 10

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rect = kk_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Set Koukaton's initial position at the center of the screen
    clock = pg.time.Clock()
    tmr = 0

    bomb_surface = pg.Surface((BOMB_RADIUS * 2, BOMB_RADIUS * 2))
    bomb_surface.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_surface, (255, 0, 0), (BOMB_RADIUS, BOMB_RADIUS), BOMB_RADIUS)
    bomb_rect = bomb_surface.get_rect()
    bomb_rect.x = random.randint(0, WIDTH - bomb_rect.width)
    bomb_rect.y = random.randint(0, HEIGHT - bomb_rect.height)

    movement_dict = {
        pg.K_UP: (0, -5),    # Up arrow: (0, -5)
        pg.K_DOWN: (0, 5),   # Down arrow: (0, 5)
        pg.K_LEFT: (-5, 0),  # Left arrow: (-5, 0)
        pg.K_RIGHT: (5, 0)   # Right arrow: (5, 0)
    }

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rect)

        keys = pg.key.get_pressed()
        total_movement = (0, 0)

        for key, movement in movement_dict.items():
            if keys[key]:
                total_movement = (total_movement[0] + movement[0], total_movement[1] + movement[1])

        kk_rect.move_ip(total_movement)

        # Check the boundaries to ensure Koukaton's whole body fits within the screen
        if kk_rect.left < 0:
            kk_rect.left = 0
        if kk_rect.right > WIDTH:
            kk_rect.right = WIDTH
        if kk_rect.top < 0:
            kk_rect.top = 0
        if kk_rect.bottom > HEIGHT:
            kk_rect.bottom = HEIGHT

        bomb_rect.move_ip(total_movement)

        bomb_rect.x += 5
        bomb_rect.y += 5

        # Check the boundaries to prevent the red ball from going out of the screen
        if bomb_rect.left < 0:
            bomb_rect.left = 0
        if bomb_rect.right > WIDTH:
            bomb_rect.right = WIDTH
        if bomb_rect.top < 0:
            bomb_rect.top = 0
        if bomb_rect.bottom > HEIGHT:
            bomb_rect.bottom = HEIGHT
        
        

        screen.blit(bomb_surface, bomb_rect)

        pg.display.update()
        tmr += 1
        clock.tick(60)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

