a = {}
i = 0
for rawline in open("./groundtruth_rect.txt"):
    line = rawline.strip()                      #去除空格和换行符
    a[i] = line.split(',')                      #以,为分隔符分割每行字符串
    print(a[i])
    i += 1
print('共有' + str(i) + '帧')
