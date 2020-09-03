import pandas as pd #读取数据的dataframe
import urllib #获取网络数据
import tempfile #创建文件临时系统
import shutil #文件操作
import  zipfile #压缩文件

temp_dir =  tempfile.mkdtemp()  #创建临时目录
data_source = "http://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip";
zipname = temp_dir + "/Bike-Sharing-Dataset.zip"  #拼接文件和路径
try:
    urllib.urlretrieve(data_source,zipname) #获取数据python 2.x
except:
    urllib.request.urlretrieve(data_source, zipname) # 获得数据  python3.x
zip_ref = zipfile.ZipFile(zipname,'r') #创建一个ZipFile对象处理压缩文件
zip_ref.extractall(temp_dir) #解压
zip_ref.close()

import stat