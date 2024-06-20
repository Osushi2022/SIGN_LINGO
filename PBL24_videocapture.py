import cv2
import os
import torch
import torch.nn as nn
import numpy as np
import threading
from pytorch_i3d import InceptionI3d

f = open('preprocess/wlasl_class_list100.txt', 'r', encoding='UTF-8')
class_list = f.read().splitlines()

class CenterCrop(object):
    def __init__(self, size):
        self.size = (size,size)
    def __call__(self, imgs):
        t, h, w, c = imgs.shape
        th, tw = self.size
        i = int(np.round((h - th) / 2.))
        j = int(np.round((w - tw) / 2.))
        return imgs[:, i:i+th, j:j+tw, :]

    def __repr__(self):
        return self.__class__.__name__ + '(size={0})'.format(self.size)

def video_to_tensor(pic):
    return torch.from_numpy(pic.transpose([3, 0, 1, 2]))

def load_rgb_frames_from_video(imgs):
    frames = []
    for img in imgs:
        w, h, c = img.shape
        img = cv2.resize(img, (int(h/w*244), 224))
        img = (img / 255.) * 2 - 1
        frames.append(img)

    return np.asarray(frames, dtype=np.float32)

def estimation_sign_langage(imgs,
        weights=None,
        num_classes=2000):

    i3d = InceptionI3d(400, in_channels=3)
    i3d.load_state_dict(torch.load('weights/rgb_imagenet.pt'))

    i3d.replace_logits(num_classes)
    i3d.load_state_dict(torch.load(weights))
    i3d.cuda()
    i3d = nn.DataParallel(i3d)
    i3d.eval()

    imgs = load_rgb_frames_from_video(imgs)
    transforms = CenterCrop(224)
    imgs = transforms(imgs)
    ret_img = video_to_tensor(imgs)

    ret_img = ret_img[np.newaxis, :, :, :, :]
    per_frame_logits = i3d(ret_img)

    predictions = torch.max(per_frame_logits, dim=2)[0]
    out_labels = np.argsort(predictions.cpu().detach().numpy()[0])
    out_probs = np.sort(predictions.cpu().detach().numpy()[0])
    label_index = torch.argmax(predictions[0]).item()
    
    label_list = []

    for i in range(len(predictions[0])):
        if predictions[0][i] > -1.2:
            label_list.append(i)

    # print(out_labels[-5:])
    # print(label_index)
    return  label_list

if __name__ == '__main__':

    f = open('preprocess/wlasl_class_list100.txt', 'r', encoding='UTF-8')
    class_list = f.read().splitlines()
    # class_list = f.readlines()
    # print(class_list)

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 30)

    countnum=0
    getflame=60
    frequency=15
    frames = []

    num_classes = 100
    # train_split = 'preprocess/nslt_{}.json'.format(num_classes)
    weights = 'archived/asl100/FINAL_nslt_100_iters=896_top1=65.89_top5=84.11_top10=89.92.pt'

    while True:
        ret, frame = cap.read()
        cv2.imshow('camera' , frame)

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
                sign_language_label_list=estimation_sign_langage(imgs, weights=weights, num_classes=num_classes)
                for i in range(len(sign_language_label_list)):
                    print(class_list[sign_language_label_list[i]])

        key =cv2.waitKey(10)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    # ================== test i3d on a dataset ==============
    # need to add argparse
    # num_classes = 100
    # train_split = 'preprocess/nslt_{}.json'.format(num_classes)
    # weights = 'archived/asl100/FINAL_nslt_100_iters=896_top1=65.89_top5=84.11_top10=89.92.pt'
    # sign_language_label=estimation_sign_langage(imgs, weights=weights, num_classes=num_classes)
    # print(sign_language_label)