import os, cv2, time
import numpy as np
from os.path import join
from ppgan.apps import DeOldifyPredictor as deoldify


def gray_to_rgb(input_dir, output_dir):
    """

    :param input_dir: 输入路径
    :param output_dir: 输出路径
    :return: 程序耗时
    """

    img_origin = cv2.imread(input_dir)
    t_0 = time.time()
    image = deoldify.run_image(img_origin)
    image = np.float32(image)
    t_1 = time.time()
    cv2.imwrite(output_dir, image)
    time_consume = t_1 - t_0
    return time_consume


i = 1

dataset_dir = 'D:/DataSet/DTB70/'
for root1, dirs1, files1 in os.walk(dataset_dir):
    for dir1 in dirs1:
        dir1 = join(root1, dir1)
        for root2, dirs2, files2 in os.walk(dir1):
            for dir2 in dirs2:
                dir2 = join(root2, dir2)
                output_dir = dir2 + '_gray'

                print("序列" + str(i) + "开始转换")
                img_path = [(join(dir2, img_names), join(output_dir, img_names)) for img_names in os.listdir(dir2)]
                for path in img_path:
                    rgb_to_gray(path[0], path[0])
                    print(".", end='')
                print("序列" + str(i) + "转换完成")
                i += 1
            break
# time_total = 0
# for sequences in os.listdir(dataset_dir):
#     input_seq_dir = os.path.join(dataset_dir, sequences)
#     output_seq_dir = os.path.join('/home/aistudio/Gray_data', sequences)  # 输出序列文件夹路径
#     recolor_dir = os.path.join('/home/aistudio/DeOldify_data', sequences)
#     if not os.path.isdir(recolor_dir):
#         os.mkdir(recolor_dir)
#
#     print("序列" + str(i) + "开始上色")
#     img_dir2 = [(os.path.join(output_seq_dir, img_names), os.path.join(recolor_dir, img_names)) for img_names in
#                 os.listdir(output_seq_dir)]
#     seq_time_total = 0
#     j = 0
#     for path in img_dir2:
#         seq_time_total += gray_to_rgb(path[0], path[1])
#         print("", end='.')
#         j += 1
#     print("序列" + str(i) + "上色完成，共" + str(j) + "帧，用时%fs" % (seq_time_total))
#     time_total += seq_time_total
#     i += 1
# print("上色共耗时%f" % (time_total))