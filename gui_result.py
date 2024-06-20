import pygame
import sys
import cv2
from pygame.locals import *
import numpy as np
import gui_def


class result:
    def main():
        pygame.init()
        result_screen=gui_def.GUI.Screen("result",340,50) #メイン画面の生成
        gui_def.GUI.text(result_screen,"time",60,(0,0,0),250,200)
        gui_def.GUI.text(screen=result_screen,txt=f"{int(gui_def.itime)//100}s",font_size=60,color=(255,0,0),x=420,y=200)
        finish_button=gui_def.GUI.button(screen=result_screen,color=(0,0,0),x=580,y=430,width=160,height=80,font_size=45,txt="finish",font_color=(255,255,255),text_x=610,text_y=450)
        pygame.display.update()

        clock = pygame.time.Clock() # Clockオブジェクトの生成
        going = True # ループを続けるかのフラグ

        # 終了イベント発生までループをまわす
        while going:
        # イベントを取得
            for event in pygame.event.get():
            # 終了イベント（画面の×ボタン押下など）の場合、
            # ループを抜ける
                if event.type == pygame.QUIT:
                    going = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if finish_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

 
        # フレームレート（1秒間に何回画面を更新するか）の設定
            clock.tick(30)

        pygame.quit()
        sys.exit()

