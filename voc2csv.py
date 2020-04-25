
#coding:utf8
import csv
import os
import glob
import sys
import random


class PascalVOC2CSV(object):
    def __init__(self,xml=[], ann_trainval_path='./annotations_trainval.csv',ann_train_path='./annotations_train.csv',ann_val_path='./annotations_val.csv',ann_test_path='./annotations_test.csv',classes_path='./classes.csv'):
        '''
        :param xml: Pascal VOC xml file list
        :param ann_path: ann_path
        :param classes_path: classes_path
        '''
        self.xml = xml

        self.ann_trainval_path = ann_trainval_path
        self.ann_train_path = ann_train_path
        self.ann_val_path = ann_val_path
        self.ann_test_path = ann_test_path
        self.classes_path=classes_path

        self.label=[]

        self.annotations_trainval=[]
        self.annotations_train=[]
        self.annotations_val=[]
        self.annotations_test=[]

        self.data_transfer()
        self.write_file()
 
    def convert_xml(self,xml_file,annotations):
        with open(xml_file, 'r') as fp:
            for p in fp:
                if '<filename>' in p:
                    self.file_name = p.split('>')[1].split('<')[0]
 
                if '<object>' in p:
                    # cls
                    d = [next(fp).split('>')[1].split('<')[0] for _ in range(9)]
                    self.supercategory = d[0]
                    if self.supercategory not in self.label:
                        self.label.append(self.supercategory)
                    # bb
                    x1 = int(d[-4]);
                    y1 = int(d[-3]);
                    x2 = int(d[-2]);
                    y2 = int(d[-1])
 
                    annotations.append([os.path.join('JPEGImages',self.file_name),x1,y1,x2,y2,self.supercategory])
 
    def data_transfer(self):
        # split  the train/val/test
        trainval_percent = 0.25
        train_percent = 0.75 

        num = len(self.xml) 
        list = range(num) 
        tv = int(num * trainval_percent) 
        tr = int(tv * train_percent) 
        trainval = random.sample(list, tv) 
        train = random.sample(trainval, tr) 

        for i, xml_file in enumerate(self.xml):
            try:
                #print(xml_file)
                sys.stdout.write('\r>> Converting image %d/%d' % (
                    i + 1, len(self.xml)))
                sys.stdout.flush()
                
                if i in trainval:
                    self.convert_xml(xml_file,self.annotations_trainval)
                    if i in train:
                        self.convert_xml(xml_file,self.annotations_val)
                    else: 
                        self.convert_xml(xml_file,self.annotations_test) 
                else:
                    self.convert_xml(xml_file,self.annotations_train)
            except:
                continue
 
        sys.stdout.write('\n')
        sys.stdout.flush()
 
    def write_file(self,):
        with open(self.ann_train_path, 'w', newline='') as fp:
            csv_writer = csv.writer(fp, dialect='excel')
            csv_writer.writerows(self.annotations_train)

        with open(self.ann_trainval_path, 'w', newline='') as fp:
            csv_writer = csv.writer(fp, dialect='excel')
            csv_writer.writerows(self.annotations_trainval)
 
        with open(self.ann_val_path, 'w', newline='') as fp:
            csv_writer = csv.writer(fp, dialect='excel')
            csv_writer.writerows(self.annotations_val)
 
        with open(self.ann_test_path, 'w', newline='') as fp:
            csv_writer = csv.writer(fp, dialect='excel')
            csv_writer.writerows(self.annotations_test)
 
        class_name=sorted(self.label)
        class_=[]
        for num,name in enumerate(class_name):

            class_.append([name,num])
            print(class_)

        with open(self.classes_path, 'w', newline='') as fp:
            csv_writer = csv.writer(fp, dialect='excel')
            csv_writer.writerows(class_)
 
 
xml_file = glob.glob('./Annotations/*.xml')
random.shuffle(xml_file)
 
PascalVOC2CSV(xml_file)
