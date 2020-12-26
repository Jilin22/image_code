import os
import time
from os.path import join
from PIL import Image


def rgb_to_gray(input_dir):
    """

    :param input_dir:
    :return:
    """
    img = Image.open(input_dir)
    t_0 = time.time()
    img = img.convert("L")
    t_1 = time.time()
    time_consume = t_1 - t_0
    img.save(input_dir)
    return time_consume


i = 1
time_total = 0
dataset_dir = '/home/v4r/Dataset/DTB70/'
for root1, dirs1, files1 in os.walk(dataset_dir):
    for dir1 in dirs1:
        dir1 = join(root1, dir1)
        for root2, dirs2, files2 in os.walk(dir1):
            for dir2 in dirs2:
                dir2 = join(root2, dir2)
                seq_time_total = 0
                j = 0
                print("序列" + str(i) + "开始转换")
                img_path = [join(dir2, img_names) for img_names in os.listdir(dir2)]
                for path in img_path:
                    seq_time_total += rgb_to_gray(path)
                    print("", end='.')
                    j += 1
                print("序列" + str(i) + "转换完成，共" + str(j) + "帧，用时%fs" % (seq_time_total))
                time_total += seq_time_total
                i += 1
            break
print("转换共耗时%f" % time_total)
