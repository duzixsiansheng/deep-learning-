# -*- coding:utf-8 -*-
import os
import random 
classes = ['卫生纸','垃圾桶','橘子皮','牛奶盒','玉米','瓜子皮','葱','香蕉皮','鸡蛋壳']
trainval_percent = 0.25
train_percent = 0.75
ftrainval = open('ImageSets/Main/trainval.txt', 'w', encoding='utf-8')
ftest = open('ImageSets/Main/test.txt', 'w', encoding='utf-8')
ftrain = open('ImageSets/Main/train.txt', 'w', encoding='utf-8')
fval = open('ImageSets/Main/val.txt', 'w', encoding='utf-8')
for i in range(len(classes)):
    xmlfilepath = 'predata/finalXml/' + classes[i]
    txtsavepath = 'ImageSets\Main'
    total_xml = os.listdir(xmlfilepath)
    num = len(total_xml)
    list = range(num)
    tv = int(num * trainval_percent)
    tr = int(tv * train_percent)
    trainval = random.sample(list, tv)
    train = random.sample(trainval, tr)


    for i in list:
        name = total_xml[i][:-4] + '\n'
        if i in trainval:
            ftrainval.write(name)
            if i in train:
                ftest.write(name)
            else:
                fval.write(name)
        else:
            ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()

