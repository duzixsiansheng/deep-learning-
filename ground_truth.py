import xml.etree.ElementTree as ET
import os


ImgPath = '100/'
XmlPath = '101/'
TxtPath = '102/'

Xmllist = os.listdir(XmlPath)
for xml in Xmllist:
    print(xml)
    f = open(TxtPath + '%s.txt'%(os.path.splitext(xml)[0]), 'w')
    tree=ET.parse(XmlPath + xml)
    root = tree.getroot()
    for obj in root.iter('object'):
        try:
            difficult = obj.find('difficult').text
            if difficult is '1':
                difficult = 'difficult'
        except:
            difficult = 0
            continue
        cls = obj.find('name').text


        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text),
             int(xmlbox.find('ymax').text))
        if difficult is 'difficult':
            f.write(cls + ' ' + ' '.join([str(a) for a in b]) + ' ' + difficult)
        else:
            f.write(cls + ' ' + ' '.join([str(a) for a in b]))
        f.write('\n')
