import os
import cv2
import time
import numpy as np
from PIL import Image
from os.path import join
from ppgan.apps import DeOldifyPredictor

deoldify = DeOldifyPredictor()


def gray_to_rgb(input_dir):
    """

    :param input_dir:
    :return:
    """

    img_origin = Image.open(input_dir)
    crop_box = [900, 400, 1100, 600]
    img = img_origin.crop(crop_box)

    t_0 = time.time()

    img = np.float32(img)
    img = deoldify.run_image(img)
    img = np.float32(img)

    t_1 = time.time()

    cv2.imwrite(input_dir, img)
    time_consume = t_1 - t_0
    return time_consume


i = 1
time_total = 0
frames_total = 0
dataset_dir = '/home/v4r/Dataset/DTB70_Gray/'
for root1, dirs1, files1 in os.walk(dataset_dir):
    for dir1 in dirs1:
        dir1 = join(root1, dir1)
        for root2, dirs2, files2 in os.walk(dir1):
            for dir2 in dirs2:
                dir2 = join(root2, dir2)
                seq_time_total = 0
                j = 0
                print("序列" + str(i) + "开始上色")
                img_path = [join(dir2, img_names) for img_names in os.listdir(dir2)]
                for path in img_path:
                    seq_time_total += gray_to_rgb(path)
                    print("", end='.')
                    j += 1
                print("序列" + str(i) + "上色完成，共" + str(j) + "帧，用时%f s" % seq_time_total)
                time_total += seq_time_total
                frames_total += j
                i += 1
            break
print("上色共处理" + str(frames_total) + "帧，耗时%f s" % time_total)
