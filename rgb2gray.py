import os, cv2, time
from os.path import join
from PIL import Image


def rgb_to_gray(input_dir):
    """

    :param input_dir:
    :return:
    """
    img = Image.open(input_dir)
    img = img.convert("L")
    img.save(output_dir)


i = 1

dataset_dir = './DataSet/DTB70/'
for root1, dirs1, files1 in os.walk(dataset_dir):
    for dir1 in dirs1:
        dir1 = join(root1, dir1)
        for root2, dirs2, files2 in os.walk(dir1):
            for dir2 in dirs2:
                dir2 = join(root2, dir2)
                output_dir = dir2 + '_gray'

                print("序列" + str(i) + "开始转换")
                img_path = [join(dir2, img_names) for img_names in os.listdir(dir2)]
                for path in img_path:
                    rgb_to_gray(path)
                    print(".", end='')
                print("序列" + str(i) + "转换完成")
                i += 1
            break
