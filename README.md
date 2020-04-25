# deep-learning-lajifenlei


数据处理
      
      使用data-classification来对数据进行预处理（筛选，修改xml）


augment：
   
     使用pre_process_v2.ipynb来进行augment。（有时会出现生成图片多于xml的问题，此时需要用checkName.py来把多出来的img处理掉）


生成csv：
    
    使用get_train_val_test.py可以随机生成train/test等分类，自动每个class单独生成。
    
    使用voc2csv.py把txt转换成csv


train：
    
    使用keras_retinanet进行train


数据分析：
    
    使用mankData.ipynb可以生成detect和label的对比图片。
    
    readTXT.py可以筛选出test的图片和xml
    
    detect.ipynb可以生成用于mAP的txt文件
    
    
    
  
   


