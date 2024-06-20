import pygame
import sys
import cv2
from pygame.locals import *
import numpy as np
import gui_quiz
import gui_def



class Gamen1:
    def main():
        pygame.init() # メイン画面（Surface）初期化(横, 縦)

        cap = cv2.VideoCapture("./00335.mp4")  # 動画ファイルを読み込む
        ret, frame = cap.read()  # フレームを読み込む

        train_screen=gui_def.GUI.Screen("Training Phase")
        button=gui_def.GUI.button(screen=train_screen,color=(255,0,0),x=550,y=450,width=60,height=30,font_size=30,txt="quiz start",font_color=(0,0,0),text_x=540,text_y=455)

        
        while True:
            if not cap.isOpened():
                print("Error: Could not open video file.train")
                return
            ret, frame = cap.read()
            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                break


            if not ret:
                cap = cv2.VideoCapture("./00335.mp4")  # 動画ファイルを読み込む
                

            clock = pygame.time.Clock()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # OpenCVのカラーフォーマットをPygameのカラーフォーマットに変換
            frame = pygame.surfarray.make_surface(frame)  # フレームをPygameのSurfaceオブジェクトに変換
            # numpy.rot90()を使うとNumPy配列ndarrayを90度間隔（90度、180度、270度）で回転できる。
            frame= pygame.transform.rotate(frame, 270)
            train_screen.blit(frame, (170, 100))  # スクリーンにフレームを描画
            pygame.display.update()
        
            for event in pygame.event.get():
                if event.type == QUIT:  # 閉じるボタンが押されたら終了
                    pygame.quit()       
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_q:  # 'q' キーが押されたら終了
                        pygame.quit()       
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button.collidepoint(event.pos):
                        gui_quiz.quiz.main()
 
                else :
                    break
                    
                
                
            clock.tick(30)
        

        
    
        
        