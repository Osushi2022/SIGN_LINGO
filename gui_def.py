import pygame
import sys
import cv2
from pygame.locals import *
import numpy as np
import random

itime=0
iindex=0
name=''

class GUI:


    def __init__(self,gesture,url,rabel):
        self.gesture=gesture
        self.url=url
        self.rabel=rabel
    
    def return_rabel(self):
        return self.rabel
    
    def return_gesture(self):
        return self.gesture
    
    def return_url(self):
        return self.url
    

    def Screen(title,x,y): #画面生成とタイトル
        pygame.init() # メイン画面（Surface）初期化(横, 縦)
        screen = pygame.display.set_mode((840, 600)) #画面のサイズ
        pygame.display.set_caption("Sign Language") # メイン画面のタイトル
        screen.fill((220, 220, 220)) #メイン画面の色設定（引数：RGB）    
        font_title = pygame.font.Font(None, 70) # フォントオブジェクト生成（引数：フォント名とフォントサイズ）
                                            # フォント名にNoneを指定するとPygameの既定のフォントになる
        title_surface = font_title.render(title, True, (0, 0, 255)) # テキストのSurfaceオブジェクトの生成（引数：テキスト内容、antialias、文字の色RGB）
        screen.blit(title_surface, (x, y)) # メイン画面上にテキストを配置（引数：配置するSurface、座標）

        return screen

    def text(screen,txt,font_size,color,x,y):#文字の生成と配置
        font_text = pygame.font.Font(None, font_size) # フォントオブジェクト生成（引数：フォント名とフォントサイズ）
                                            # フォント名にNoneを指定するとPygameの既定のフォントになる
        text_surface = font_text.render(txt, True, color) # テキストのSurfaceオブジェクトの生成（引数：テキスト内容、antialias、文字の色RGB）
        screen.blit(text_surface, (x,y)) # メイン画面上にテキストを配置（引数：配置するSurface、座標）
    
    def button(screen,color,x,y,width,height,font_size,txt,font_color,text_x,text_y):#ボタン設定と文字
        button = pygame.Rect(x, y, width, height) #四角形の左頂点のx軸の座標、左頂点のy軸の座標、幅、高さ
        pygame.draw.rect(screen, color, button)
        font_button = pygame.font.SysFont(None, font_size)#ボタンのフォントを設定する
        text_button = font_button.render(txt, True, font_color) #ボタンのテキスト
        screen.blit(text_button, (text_x, text_y)) #ボタンのテキストを配置

        return button
    
    def image(screen,image_pass,scal_x,scal_y,x,y):
        img = pygame.image.load(image_pass)
        img = pygame.transform.scale(img, (scal_x, scal_y)) #200 * 130に画像を縮小
        screen.blit(img, (x, y))

    def random(a):
        return random.randint(0,a)
    
    
    # def search():
    #     if name==gesture_list[iindex]:
    #        del random_list[iindex]
    #     else:
    #         pass

    def reduce_element():
        del gesture_list[iindex]
    
    def color_txt():
        flag=0
        if len(gesture_list) >=2:
            color=(0,255,0)
            txt="next"

        else :
            color=(255,0,0)
            txt="result"
            flag=1

        return color,txt,flag
    
    def choose_movie():
        num=10
        gesture_list.clear

        for a in range(num):
            ran=GUI.random(len(movie_list)-1)
            print(ran)
            print("'''''''")
            gesture_list.append(movie_list[ran])
            del movie_list[ran]
    
# gesture_list=[GUI("chair","data/4/09848.mp4",4),
#             #   GUI("cousin","data/9/13640.mp4",9),
#             #   GUI("fine","data/11/21869.mp4",11),
#               GUI("help","data/12/27214.mp4",12),
#             #   GUI("no","data/13/69411.mp4",13),
#             #   GUI("thin","data/14/66606.mp4",14),
#               GUI("yes","data/17/64287.mp4",17),
#             #   GUI("like","data/23/33269.mp4",23),
#               GUI("table","data/28/56556.mp4",28),
#               GUI("fish","data/38/22113.mp4",38),
#               GUI("graduate","data/39/25329.mp4",39),
#             #   GUI("language","data/43/66007.mp4",43),
#               GUI("study","data/47/55365.mp4",47),
#             #   GUI("wrong","data/50/64091.mp4",50),
#               GUI("accident","data/51/00624.mp4",51),
#             #   GUI("change","data/54/09953.mp4",54),
#               GUI("cow","data/57/13703.mp4",57),
#               GUI("dance","data/58/14625.mp4",58),
#             #   GUI("dark","data/59/14681.mp4",59),
#             #   GUI("give","data/64/24648.mp4",64),
#             #   GUI("last","data/65/32246.mp4",65),
#             #   GUI("meet","data/66/35513.mp4",66),
#             #   GUI("work","data/75/63788.mp4",75),
#             #   GUI("cheat","data/81/10159.mp4",81),
#             #   GUI("full","data/85/23771.mp4",85),
#             #   GUI("how","data/86/28205.mp4",86),
#             #   GUI("paint","data/91/40837.mp4",91),
#             #   GUI("right","data/95/48114.mp4",95)
#             ]    

gesture_list = []
movie_list=[GUI("before","data/3/05743.mp4",3),
              GUI("chair","data/4/09848.mp4",4),
              GUI("go","data/5/24941.mp4",5),
              GUI("cousin","data/9/13640.mp4",9),
              GUI("fine","data/11/21869.mp4",11),
              GUI("help","data/12/27214.mp4",12),
              GUI("no","data/13/69411.mp4",13),
              GUI("thin","data/14/66606.mp4",14),
              GUI("yes","data/17/64287.mp4",17),
              GUI("like","data/23/33269.mp4",23),
              GUI("table","data/28/56556.mp4",28),
              GUI("fish","data/38/22113.mp4",38),
              GUI("graduate","data/39/25329.mp4",39),
              GUI("language","data/43/66007.mp4",43),
              GUI("study","data/47/55365.mp4",47),
              GUI("wrong","data/50/64091.mp4",50),
              GUI("accident","data/51/00624.mp4",51),
              GUI("change","data/54/09953.mp4",54),
              GUI("cow","data/57/13703.mp4",57),
              GUI("dance","data/58/14625.mp4",58),
              GUI("dark","data/59/14681.mp4",59),
              GUI("give","data/64/24648.mp4",64),
              GUI("last","data/65/32246.mp4",65),
              GUI("meet","data/66/35513.mp4",66),
              GUI("work","data/75/63788.mp4",75),
              GUI("cheat","data/81/10159.mp4",81),
              GUI("full","data/85/23771.mp4",85),
              GUI("how","data/86/28205.mp4",86),
              GUI("paint","data/91/40837.mp4",91),
              GUI("right","data/95/48114.mp4",95)]

            #   GUI("fifth","./00335.mp4"),GUI("sixth","./your_video_file.mp4"),
            #   GUI("seventh","./00335.mp4"),GUI("eighth","./your_video_file.mp4"),GUI("ninth","./00335.mp4"),
            #   GUI("tenth","./your_video_file.mp4")]

random_list=[0,1,2,3,4,5,6,7,8,9]



    
    # def comb_movie(movie_files,out_path):
    #     fourcc =cv2.VideoWriter_fourcc('m','p','4','v')
        
    #     movie = cv2.VideoCapture(movie_files[0])
    #     fps = movie.get(cv2.CAP_PROP_FPS)
    #     height = movie.get(cv2.CAP_PROP_FRAME_HEIGHT)
    #     width = movie.get(cv2.CAP_PROP_FRAME_WIDTH)

    #     # 出力先のファイルを開く
    #     out = cv2.VideoWriter(out_path, int(fourcc), fps, (int(width), int(height)))

    #     for movies in (movie_files):
    #         print(movies)
    #         # 動画ファイルの読み込み，引数はビデオファイルのパス
    #         movie = cv2.VideoCapture(movies)

    #         # 正常に動画ファイルを読み込めたか確認
    #         if movie.isOpened() == True: 
    #             # read():1コマ分のキャプチャ画像データを読み込む
    #             ret, frame = movie.read() 
    #         else:
    #             ret = False

    #         while ret:
    #             # 読み込んだフレームを書き込み
    #             out.write(frame)
    #             # 次のフレーム読み込み
    #             ret, frame = movie.read()

    #     # ディレクトリ内の動画をリストで取り出す
    #     files = sorted(glob.glob("./movie_dir/*.mp4"))

    #     # 出力ファイル名
    #     out_path = "movie_out1.mp4"

    #     return files,out_path

