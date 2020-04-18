import os
import shutil

with open('test.txt','r') as f:
        for line in f:
            shutil.copy('Annotations/' + line.strip() + '.xml', 'testXml/' + line.strip() + '.xml')
            shutil.copy('JPEGImages/' + line.strip() + '.jpg', 'testJpg/' + line.strip() + '.jpg')
