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
        # train_screen=gui_def.GUI.Screen("Training Phase",200,20)
        webcam = cv2.VideoCapture(0)
       
        
        while True:
            for num in gui_def.gesture_list:

                cap = cv2.VideoCapture(num.url)  # 動画ファイルを読み込む
                ret, frame = cap.read()  # フレームを読み込む
                train_screen=gui_def.GUI.Screen("Training Phase",240,50) #main 190,50
                button=gui_def.GUI.button(screen=train_screen,color=(0,0,0),x=600,y=500,width=200,height=80,font_size=45,txt="quiz start",font_color=(255,255,255),text_x=620,text_y=520)
                gui_def.GUI.text(train_screen,"gesture name",50,(0,0,0),210,120)
                gui_def.GUI.text(train_screen,num.gesture,50,(0,0,0),460,120)
                gui_def.GUI.text(train_screen,"example",40,(0,0,0),170,460)
                gui_def.GUI.text(train_screen,"web camera",40,(0,0,0),560,460)

                while True:
                    
                    if not cap.isOpened():
                        print("Error: Could not open video file tarin.")
                        return
                    ret, frame = cap.read()
                    if not ret:
                        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                        break

                    if not ret:
                        cap = cv2.VideoCapture(num.url)  # 動画ファイルを読み込む

                    ret_webcam, frame_webcam = webcam.read()
                    if not ret_webcam:
                        print("something wrong with webcam")
                        break


                    clock = pygame.time.Clock()
                    clock.tick(30)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # OpenCVのカラーフォーマットをPygameのカラーフォーマットに変換
                    frame_webcam = cv2.cvtColor(frame_webcam, cv2.COLOR_BGR2RGB)
                    frame_webcam = cv2.resize(frame_webcam,(400,300))
                    frame=cv2.resize(frame,(400,300))
                    frame = pygame.surfarray.make_surface(frame)  # フレームをPygameのSurfaceオブジェクトに変換
                    frame_webcam = pygame.surfarray.make_surface(frame_webcam)
                    # numpy.rot90()を使うとNumPy配列ndarrayを90度間隔（90度、180度、270度）で回転できる。
                    frame= pygame.transform.rotate(frame, 270)
                    frame_webcam = pygame.transform.rotate(frame_webcam, 270)
                    train_screen.blit(frame, (10, 160))  # スクリーンにフレームを描画
                    train_screen.blit(frame_webcam, (430, 160))
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
                        else:
                            break
        
                        
            cv2.destroyAllWindows()
            cap.release()
                        
                        
                    
                

                
            
                
                