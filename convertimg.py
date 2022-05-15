from PIL import Image
import numpy as np
import cv2
import os
# ����ͼƬ
# img = Image.open(r'C:\Users\znjt\Desktop\huhui\40051.jpg')
# img = Image.fromarray(np.uint8(img))
# t = img.convert('L')
# img=Image.fromarray(np.uint8(t)*255)
# img.save(r'C:\Users\znjt\Desktop\huhui\40051(8).jpg')
path = '/home/cell/datasets/cell/images/01单核系/单核系/'
save_path = '/home/cell/datasets/cell/images/01单核系/单核系new/'
os.mkdir(save_path)
for i in os.listdir(path):
    print('loaded pic:%s' % (path+i))
    img = Image.open(path+i).convert('RGB')
    img = img.resize([256,256])
    save_name = i[:-4]+'.png'
    print('save to pic:%s' % (save_path+save_name))
    img.save(save_path+save_name)

