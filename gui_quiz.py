import sys
import time

import pygame
from pygame.locals import *
import cv2
import numpy as np

import gui_def
import gui_correct
import gui_quiz
import gui_wrong
import PBL24_videocapture


device = 0 # camera device number

class quiz:
    def main():
        
            pygame.init()

            global device
            cap = cv2.VideoCapture(device)
            fps = cap.get(cv2.CAP_PROP_FPS)
            wt  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            ht  = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            print("Size:", ht, "x", wt, "/Fps: ", fps)
            num=gui_def.GUI.random(len(gui_def.gesture_list)-1)
            
            gui_def.iindex=num
            # gui_def.name=gui_def.GUI.return_gesture(gui_def.gesture_list[num])

            quiz_screen=gui_def.GUI.Screen('Make a gesture of the '+gui_def.GUI.return_gesture(gui_def.gesture_list[num]),100,20) #メイン画面の生成
            next_button=gui_def.GUI.button(screen=quiz_screen,color=(0,255,0),x=510,y=400,width=80,height=50,font_size=31,txt="next",font_color=(255,255,255),text_x=528,text_y=410)
            start_time=time.time()
            running = True

            ############################################################################################
            countnum=0
            getflame=60
            frequency=15
            frames = []
            sign_language_list = []
            num_classes = 100
            weights = 'archived/asl100/FINAL_nslt_100_iters=896_top1=65.89_top5=84.11_top10=89.92.pt'
            wrong_num=0
            ############################################################################################
                

            while running:
                if not cap.isOpened():
                    print("Error: Could not open video file.quiz")
                    return
                ret, frame = cap.read()
                if not ret:
                    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue

                ############################################################################################
                sign_language_list = []
                answer = "no_answer"
                if countnum < getflame:
                    frames.append(frame)
                    countnum+=1
                else:
                    frames.append(frame)
                    frames.pop(0)
                    # print(np.asarray(frames, dtype=np.float32).shape)
                    countnum+=1
                    if countnum%frequency == 0 :
                        imgs = np.asarray(frames, dtype=np.float32)
                        sign_language_label_list=PBL24_videocapture.estimation_sign_langage(imgs, weights=weights, num_classes=num_classes)
                        for i in range(len(sign_language_label_list)):
                            # print(sign_language_label_list[i])
                            # print(gui_def.GUI.return_rabel(gui_def.gesture_list[num]))
                            if sign_language_label_list[i] == gui_def.GUI.return_rabel(gui_def.gesture_list[num]):
                                answer = "correct"
                            else:
                                wrong_num+=1
                                if wrong_num > 4:
                                    answer = "wrong"
                    print(answer)
                    
                ############################################################################################


                clock = pygame.time.Clock()
                clock.tick(30)
                frame= cv2.resize(frame,None,fx=2/3,fy=2/3)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # OpenCVのカラーフォーマットをPygameのカラーフォーマットに変換
                frame = pygame.surfarray.make_surface(frame)  # フレームをPygameのSurfaceオブジェクトに変換
                frame= pygame.transform.rotate(frame, 270)
                quiz_screen.blit(frame, (110, 70))  # スクリーンにフレームを描画
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
                        if next_button.collidepoint(event.pos):
                            gui_quiz.quiz.main()
                if answer == "correct":
                    gui_correct.correct.main() #ジェスチャーで正解だったら（ここはif文を変える必要あり）  
                elif answer == "wrong":
                    gui_wrong.wrong.main()

                elapsed_time1=time.time()-start_time
                gui_def.itime+=elapsed_time1
                # print(gui_def.itime//100)
                #gui_def.GUI.text(screen=quiz_screen,txt=str(gui?def.itime),font_size=50,color=(255,0,0),x=530,y=30)
                # pygame.time.wait(1000)
                
                # square = pygame.Rect(530, 30, 100, 100) #四角形の左頂点のx軸の座標、左頂点のy軸の座標、幅、高さ
                # pygame.draw.rect(quiz_screen, (220, 220, 220), square)
        
            cv2.destroyAllWindows()
            cap.release()

                
    
        
        


