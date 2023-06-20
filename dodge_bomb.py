import sys
import pygame as pg
import random


WIDTH, HEIGHT = 1600, 900
BOMB_RADIUS = 10 #爆弾の半径

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT)) #指定したゲームのウィンドウを作成
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg") #背景画像
    kk_img = pg.image.load("ex02/fig/3.png") #キャラクター画像
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0) #キャラクターの画像を２倍に拡大
    clock = pg.time.Clock()
    tmr = 0
    
        # 爆弾を作成
    bomb_surface = pg.Surface((BOMB_RADIUS * 2, BOMB_RADIUS * 2))
    bomb_surface.set_colorkey((0, 0, 0))  #爆弾表面の黒い部分を透明にする 
    pg.draw.circle(bomb_surface, (255, 0, 0), (BOMB_RADIUS, BOMB_RADIUS), BOMB_RADIUS)    # 爆弾の表面に赤い円を描く
    
        # 爆弾 Rect のランダムな位置を設定します
    bomb_rect = bomb_surface.get_rect()
    bomb_rect.x = random.randint(0, WIDTH - bomb_rect.width)
    bomb_rect.y = random.randint(0, HEIGHT - bomb_rect.height)
    
    #Koukaton Rect の初期位置を設定する
    kk_rect = kk_img.get_rect() 
    kk_rect.x = 900
    kk_rect.y = 400
    
    # 押したキーと移動量の対応
    movement_dict = {
        pg.K_UP: (0, -5),    # Up arrow: (0, -5)
        pg.K_DOWN: (0, 5),   # Down arrow: (0, 5)
        pg.K_LEFT: (-5, 0),  # Left arrow: (-5, 0)
        pg.K_RIGHT: (5, 0)   # Right arrow: (5, 0)
    }
    
    def is_inside_screen(rect):
        # 左右の境界をチェック
        if rect.left < 0 or rect.right > WIDTH:
            return False
        # 上下の境界をチェック
        if rect.top < 0 or rect.bottom > HEIGHT:
            return False
        return True

    while True:
        for event in pg.event.get(): #イベントを取得し、QUITイベントが発生した場合はプログラムを終了させる
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rect)
        
        
        keys = pg.key.get_pressed() #現在押されているキーを取得
        total_movement = (0, 0)
            
        for key, movement in movement_dict.items(): #movement_dictに定義されたキーに対応する移動量を計算し、total_movementに合算する。
            if keys[key]:
                total_movement = (total_movement[0] + movement[0], total_movement[1] + movement[1]) #要素0 → x軸方向の移動量、要素１ → ｙ軸方向の移動量
        
        kk_rect.move_ip(total_movement) #キャラクターの位置を移動する。
        
        # こうかとんの移動前の位置を保持
        prev_kk_rect = kk_rect.copy()
        kk_rect.move_ip(total_movement[0], total_movement[1])
        
        # 境界線をチェックしてこうかとんが画面外に出るのを防ぐ
        if kk_rect.left < 0:
            kk_rect.left = 0
        if kk_rect.right > WIDTH:
            kk_rect.right = WIDTH
        if kk_rect.top < 0:
            kk_rect.top = 0
        if kk_rect.bottom > HEIGHT:
            kk_rect.bottom = HEIGHT        
       

        
        # 画面上に爆弾を描きます
        screen.blit(bomb_surface, bomb_rect)
        
        #爆弾を動かす 
        bomb_rect.x += 5
        bomb_rect.y += 5

        # 境界を確認して跳ね返す
        if bomb_rect.left < 0 or bomb_rect.right > WIDTH:
            bomb_rect.x -= 5
        if bomb_rect.top < 0 or bomb_rect.bottom > HEIGHT:
            bomb_rect.y -= 5
            
        bomb_rect.move_ip(total_movement) #爆弾の位置を移動する
            
        screen.blit(bomb_surface, bomb_rect)
            
        
        
        pg.display.update()
        tmr += 1
        clock.tick(60)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()