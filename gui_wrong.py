import pygame
import sys
import cv2
from pygame.locals import *
import numpy as np
import gui_def
import gui_quiz
import gui_result
import gui_answer


class wrong:
    def main():
        
        pygame.init()
        wrong_screen=gui_def.GUI.Screen("wrong",340,50) #画面の生成
        gui_def.GUI.text(wrong_screen,"It’s a gesture of the ",50,(0,0,0),140,165)
        gui_def.GUI.text(wrong_screen,gui_def.GUI.return_gesture(gui_def.gesture_list[gui_def.iindex]),50,(0,0,0),520,165)
        back_button=gui_def.GUI.button(screen=wrong_screen,color=(0,255,0),x=110,y=300,width=300,height=200,font_size=50,txt="quiz",font_color=(255,255,255),text_x=210,text_y=380)
        answer_button=gui_def.GUI.button(screen=wrong_screen,color=(255,0,0),x=450,y=300,width=300,height=200,font_size=50,txt="answer",font_color=(255,255,255),text_x=490,text_y=380)
        pygame.display.update()

        clock = pygame.time.Clock() # Clockオブジェクトの生成
        clock.tick(30)
        
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
                    if back_button.collidepoint(event.pos):
                        gui_quiz.quiz.main()
                    elif answer_button.collidepoint(event.pos):
                        gui_answer.answer.main()

                    else:
                        break
                else:
                    break  
        # フレームレート（1秒間に何回画面を更新するか）の設定
            
        # # 終了処理
        pygame.quit()
        sys.exit()
