import pygame
import sys
import cv2
from pygame.locals import *
import numpy as np
import gui_def
import gui_quiz
import gui_result


class correct:
    def main():
        
        pygame.init()
        correct_screen=gui_def.GUI.Screen("correct",340,50) #画面の生成
        color,txt,flag =gui_def.GUI.color_txt()
        next_button=gui_def.GUI.button(screen=correct_screen,color=color,x=590,y=480,width=160,height=80,font_size=45,txt=txt,font_color=(255,255,255),text_x=640,text_y=500)
        pygame.display.update()

        cap = cv2.VideoCapture(gui_def.GUI.return_url(gui_def.gesture_list[gui_def.iindex]))  # 動画ファイルを読み込む
        gui_def.GUI.reduce_element()
        print('&&&&&')
        print(len(gui_def.gesture_list))
        ret, frame = cap.read()  # フレームを読み込むS
        while True:
            if not cap.isOpened():
                print("Error: Could not open video file.corrct")
                return
            ret, frame = cap.read()
            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            if not ret:
                cap = cv2.VideoCapture("./00335.mp4")  # 動画ファイルを読み込む



            
            frame=cv2.resize(frame,(550,350))
            clock = pygame.time.Clock()
            clock.tick(30)
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # OpenCVのカラーフォーマットをPygameのカラーフォーマットに変換
            frame = pygame.surfarray.make_surface(frame)  # フレームをPygameのSurfaceオブジェクトに変換
            # width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            # height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            # if width>300:
            
            # numpy.rot90()を使うとNumPy配列ndarrayを90度間隔（90度、180度、270度）で回転できる。
            frame= pygame.transform.rotate(frame, 270)
            correct_screen.blit(frame, (150, 120))  # スクリーンにフレームを描画
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
                    if flag ==1:

                        print('%%%%%%')
                        print(len(gui_def.gesture_list))
                        if next_button.collidepoint(event.pos):
                            gui_result.result.main()

                        print('@@@@@')
                        print(len(gui_def.gesture_list))   
                    elif flag==0:
                        print('$$$$$')
                        print(len(gui_def.gesture_list))
                        if next_button.collidepoint(event.pos):
                            gui_quiz.quiz.main()
                        else:
                            break
                    else:
                        break

                    cv2.destroyAllWindows()
                    cap.release()
        
        
        
        

        
    
        
        