import os
import xml.etree.ElementTree as ET
import shutil
from os.path import basename

img_dir = 'predata/img/香蕉皮/'
xml_dir = 'predata/finalXml/香蕉皮/'
dest_img_dir = 'duoyu'

token = 0

print(len(os.listdir(img_dir)))

for img in os.listdir(img_dir):
#for xml in os.listdir(xml_dir):
    token = 0
    #for img in os.listdir(img_dir):
    for xml in os.listdir(xml_dir):
        if os.path.splitext(xml)[0] == os.path.splitext(img)[0]:
            token = 1
    if token == 0:
        shutil.move(img_dir + '/' + img, dest_img_dir + '/' + img)

