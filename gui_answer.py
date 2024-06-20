import pygame
import sys
import cv2
from pygame.locals import *
import numpy as np
import gui_def
import gui_quiz
import gui_result


class answer:
    def main():
        
        pygame.init()
        answer_screen=gui_def.GUI.Screen("answer",340,50) #画面の生成
        color,txt,flag =gui_def.GUI.color_txt()
        next_button=gui_def.GUI.button(screen=answer_screen,color=color,x=590,y=480,width=160,height=80,font_size=45
        ,txt=txt,font_color=(255,255,255),text_x=640,text_y=500)
        pygame.display.update()

        cap = cv2.VideoCapture(gui_def.GUI.return_url(gui_def.gesture_list[gui_def.iindex]))  # 動画ファイルを読み込む
        gui_def.GUI.reduce_element()
        
        ret, frame = cap.read()  # フレームを読み込む
        while True:
            if not cap.isOpened():
                print("Error: Could not open video file.answer")
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
            answer_screen.blit(frame, (150, 120))  # スクリーンにフレームを描画
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

                        if next_button.collidepoint(event.pos):
                            gui_result.result.main()

                        else:
                            break
                    elif flag==0:
                        if next_button.collidepoint(event.pos):
                            gui_quiz.quiz.main()
                        else:
                            break

                    else:
                        break

                else:
                    break

        
            
                cv2.destroyAllWindows()
                cap.release()

        
         # 終了処理
    
        
        

        
    
        
        