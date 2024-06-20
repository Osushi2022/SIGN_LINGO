import cv2

def resizeImg(img, length):
    h, w = img.shape[:2]

    if max(h, w) < length: # do not need resizing
        return img

    if h < w:
        newSize = (int(h*length/w), length)
    else:
        newSize = (length, int(w*length/h))

    print('resize to', newSize)

    return  (newSize[1], newSize[0])


cap=cv2.VideoCapture("./output_video.m4p")
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps=float(cap.get(cv2.CAP_PROP_FPS))
frame_count=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(width,height)
new_width=320
fmt=cv2.VideoWriter_fourcc('m','p','4','v')
file_pass="C:\oit\home\ipbl24\gui.py\output_video.mp4"
out=cv2.VideoWriter(file_pass,fmt,fps,(width,height),True)

while cap.isOpened() :
        ret, frame = cap.read()

        if not ret:
            break

        
        out.write(frame)

cv2.destroyAllWindows()
cap.release()