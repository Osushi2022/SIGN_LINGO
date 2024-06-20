import sys
import pygame
import gui_def
import gui_train_t

def main():
    
    
    
    # out_path ="movie_out.mp4"
    # gui_def.GUI.comb_movie(gui_def.GUI.gesture_list,out_path)

    pygame.init()
    main_screen=gui_def.GUI.Screen("Sign Language",190,50) #メイン画面の生成
    gui_def.GUI.text(main_screen,"how to play",50,(0,0,0),150,160)
    gui_def.GUI.text(main_screen,"1. Click on the start button",40,(0,0,0),60,220)
    gui_def.GUI.text(main_screen,"2. Watch the tutorial video ",40,(0,0,0),60,260)
    gui_def.GUI.text(main_screen,"and practice to do the quiz!",40,(0,0,0),85,300)
    gui_def.GUI.text(main_screen,"3. Do the quiz and have fun ",40,(0,0,0),60,340)
    gui_def.GUI.text(main_screen,"learning sign language ",40,(0,0,0),85,380)
    gui_def.GUI.text(main_screen,"with sign-lingo!!",40,(0,0,0),85,430)

    gui_def.GUI.image(main_screen,"./hand-sign_good.png",450,350,450,70)
 
    gui_def.GUI.choose_movie()

    button=gui_def.GUI.button(screen=main_screen,color=(0,0,0),x=600,y=450,width=200,height=80,font_size=45,txt="Training start",font_color=(255,255,255),text_x=600,text_y=470)
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
                if button.collidepoint(event.pos):
                    gui_train_t.Gamen1.main()
 
    # フレームレート（1秒間に何回画面を更新するか）の設定
        clock.tick(30)

    # 終了処理
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()