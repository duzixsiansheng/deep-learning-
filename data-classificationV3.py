#在classes里更改label类型就可以自动筛选分类
# -*- coding: utf-8 -*-

defaultClasses = ['一次性筷子',
'一次性餐盒',
'今典牛奶盒',
'包装盒',
'包装盒he',
'包装袋',
'卫生纸',
'口罩',
'哈密瓜',
'垃圾桶',
'塑料瓶',
'塑料盒',
'塑料袋',
'大米',
'尿不湿',
'巧克力',
'康师傅调料包',
'快递包装袋',
'抽纸袋',
'旺旺仙贝包装袋',
'果冻袋',
'果核',
'柚子皮',
'橘子皮',
'毛线',
'水杯',
'水果网套',
'湿巾',
'火龙果皮',
'烟头',
'烟盒',
'牛奶盒',
'玉米',
'玉米棒',
'玉米芯',
'王老吉饮料瓶',
'瓜子皮',
'瓶子',
'瓶盖',
'白菜',
'白菜叶',
'米多奇雪米饼包装袋',
'纸张',
'纸杯',
'纸片',
'胡萝卜',
'芹菜',
'苹果皮',
'菜叶',
'葱',
'葱叶',
'蒜皮',
'蒜苔',
'酸奶包装袋',
'酸奶盒',
'酸奶袋',
'阿尔卑斯糖包装袋',
'雀巢咖啡',
'饮料瓶',
'馒头',
'香蕉皮',
'鸡蛋壳',
'黄瓜']

import os
import xml.etree.ElementTree as ET
import shutil

def scanClass(xml_dir, number):
    scans = []
    finalList = []
    for xml in os.listdir(xml_dir):
        in_file = open(xml_dir + '/' + xml, encoding="utf-8")
        tree = ET.parse(in_file)
        root = tree.getroot()
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in scans:
                scans.append(cls)
    print(scans)

    for i in range(len(scans)):
        count = 0
        for xml in os.listdir(xml_dir):
            in_file = open(xml_dir + '/' + xml, encoding="utf-8")
            tree = ET.parse(in_file)
            root = tree.getroot()
            for obj in root.iter('object'):
                cls = obj.find('name').text
                if cls == scans[i]:
                    count = count + 1
        print(scans[i] + 'has ' + str(count) + ' labels')
        if count >= int(number):

            finalList.append(scans[i])
    #print(finalList)
    return finalList

def printClassSize():
    rootdir = os.getcwd()
    datadir = os.path.join(rootdir, 'predata\\img')
    xmladir = os.path.join(rootdir, 'predata\\xml')
    #path, dirs, files = next(os.walk(datadir))

    list_dir = []
    list_dir = os.listdir(datadir)
    print(list_dir)

    class_size = [0]*len(list_dir)
 
    count = 0
    for name in list_dir:
        dir_name = os.path.join(datadir, name)
        onlyfiles = next(os.walk(dir_name))[2] #dir is your directory path as string
        class_size[count] = len(onlyfiles) 
        count +=1
                 
    print(class_size)

def fenLei(img_dir,xml_dir,classes):

    for xml in os.listdir(xml_dir):
        in_file = open(xml_dir + '/' + xml, encoding="utf-8")
        tree = ET.parse(in_file)
        root = tree.getroot()
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls in classes:
                shutil.copy(xml_dir + '/' + xml, 'predata/' + 'xml/' + cls + '/' + xml)
                for img in os.listdir(img_dir):

                    if os.path.splitext(xml)[0] == os.path.splitext(img)[0]:
                        shutil.copy(img_dir + '/' + img, 'predata/' + 'img/' + cls + '/' + img)
    print('分类完成')

def fixXml(classes):
    for clsA in classes:
        for xml in os.listdir('predata/' + '/xml/' + clsA + '/'):
            a = 0
            in_file = open('predata/' + 'xml/' + clsA + '/' + xml,encoding="utf-8")
            tree = ET.parse(in_file)
            root = tree.getroot()
            for obj in root.iter('object'):
                cls = obj.find('name').text
                if cls not in classes:
                    root.remove(obj)
                    a = a + 1

            for b in range(a):
                for obj in root.iter('object'):
                    cls = obj.find('name').text
                    if cls not in classes:
                        root.remove(obj)
            tree.write('predata/' + 'finalXml/' + classes  + '/' + xml, encoding="utf-8")

    print('去除xml中无用classes完成')

def toEnglish(clsaaes):
    for xml in os.listdir('predata/' + 'xml/' + clsaaes + '/'):
        in_file = open('predata/' + 'xml/' + clsaaes + '/' + xml, encoding="utf-8")
        tree = ET.parse(in_file)
        root = tree.getroot()
        name = root.find('filename')
        a = os.path.splitext(xml)[0]
        #更正xml的filename
        name.text = a + '.jpg'
        for obj in root.iter('object'):
            cls = obj.find('name')
            if cls.text in dic:
                cls.text = dic[cls.text]
        #把中文的xml改成英文的
        tree.write('predata/' + 'finalXml/' + clsaaes + '/' + xml, encoding="utf-8")

    print('中文转英文完成')


if __name__ == '__main__':
    img_dir = '410newimg'
    xml_dir = '410newxml'
    auto = input('是否使用自动筛选class功能？(y/n):')
    if auto == 'y':
        number = input('筛选class的最少data数量是？(输入数字)')
        classes = scanClass(xml_dir,number)

    else:
        classes = defaultClasses
    print(classes)



    for i in range(len(classes)):
        os.makedirs('predata' + '/xml/' + classes[i], 0o777 ,True)
        os.makedirs('predata' + '/img/' + classes[i], 0o777 ,True)
        os.makedirs('predata' + '/finalXml/' + classes[i], 0o777, True)
        #os.makedirs('predata/' + classes[i] + '/finalXml/', 0o777 ,True)
    dic = {}
    for i in range(len(classes)):
        dic[classes[i]] = ''
    fenLei(img_dir,xml_dir, classes)
    printClassSize()
    #############################################
    #r cls in classes:
        #去除多余的class
    fixXml(classes)
    ###########################################
    toE = input('是否转换成英文class(y/n):')
    if toE == 'y':
        for cls in classes:
            name = input('（请输入）你想给' + cls + '起个什么英文名字：')

            dic[cls] = name

        for cls in classes:
            toEnglish(cls)



