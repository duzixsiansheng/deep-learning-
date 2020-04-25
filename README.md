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
    
    
    
 mAP：
          
          需要3种input： 原始的img，ground_truth, detect_result
          detect.ipynb可以生成detect_result的txt
          ground_truth.py可以生成ground truth的txt
          rename.py可以把3种input改名，方便浏览（如果文件名不包括'.'那么必须改名，否则会出错）
          准备完毕后运行main.py就可以测试了
    
 
    
  
   


