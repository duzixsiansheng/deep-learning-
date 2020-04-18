#在classes里更改label类型就可以自动筛选分类


import os
import xml.etree.ElementTree as ET
import shutil


def fenLei(img_dir,xml_dir,classes):

    for xml in os.listdir(xml_dir):
        in_file = open(xml_dir + '/' + xml, encoding="utf-8")
        tree = ET.parse(in_file)
        root = tree.getroot()
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls in classes:
                shutil.copy(xml_dir + '/' + xml, 'predata/' + cls + '/xml/' + xml)
                for img in os.listdir(img_dir):

                    if os.path.splitext(xml)[0] == os.path.splitext(img)[0]:
                        shutil.copy(img_dir + '/' + img, 'predata/' + cls + '/img/' + img)
    print('分类完成')

def fixXml(classes):
    for xml in os.listdir('predata/' + classes + '/xml/'):
        a = 0
        in_file = open('predata/' + classes + '/xml' + '/' + xml,encoding="utf-8")
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
        tree.write('predata/' + classes + '/finalXml/' + xml, encoding="utf-8")

    print('去除xml中无用classes完成')

def toEnglish(clsaaes):
    for xml in os.listdir('predata/' + clsaaes + '/xml/'):
        in_file = open('predata/' + clsaaes + '/xml/' + xml, encoding="utf-8")
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
        tree.write('predata/' + clsaaes + '/finalXml/' + xml, encoding="utf-8")

    print('中文转英文完成')


if __name__ == '__main__':
    img_dir = '410newimg'
    xml_dir = '410newxml'
    #在这里修改想要的classes
    classes = ['香蕉皮', '卫生纸', '橘子皮', '鸡蛋壳', '牛奶盒', '瓜子皮','玉米']
    for i in range(len(classes)):
        os.makedirs('predata/' + classes[i] + '/xml/', 0o777 ,True)
        os.makedirs('predata/' + classes[i] + '/img/', 0o777 ,True)
        os.makedirs('predata/' + classes[i] + '/finalXml/', 0o777 ,True)
    dic = {}
    for i in range(len(classes)):
        dic[classes[i]] = ''
    fenLei(img_dir,xml_dir, classes)
    for cls in classes:
        #去除多余的class
        fixXml(cls)
    for cls in classes:
        name = input('（请输入）你想给' + cls + '起个什么英文名字：')

        dic[cls] = name

    for cls in classes:
        toEnglish(cls)


