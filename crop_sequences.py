from os.path import join
import os
from PIL import Image

a = {}
i = 0
crop_box = {}
for rawline in open("./Horse2/groundtruth_rect.txt"):
    line = rawline.strip()                      # 去除空格和换行符
    a[i] = line.split(',')                      # 以,为分隔符分割每行字符串
    swap = []
    swap.append(int(a[i][0]) - int(a[i][2]))
    swap.append(int(a[i][1]) - int(a[i][3]))
    swap.append(int(a[i][0]) + int(a[i][2]) * 2)
    swap.append(int(a[i][1]) + int(a[i][3]) * 2)
    crop_box[i] = swap
    i += 1


path = './Horse2/img'  # 表示需要命名处理的文件夹
path_new = './Horse2_crop/img'
filelist = os.listdir(path)  # 获取文件路径
filelist.sort()             #
j = 0
for item in filelist:
    img_path = join(path, item)
    img_path_new = join(path_new, item)
    img = Image.open(img_path)

    image_cropped = img.crop(crop_box[j])
    image_cropped.save(img_path_new)
    j += 1

print("finished!")
