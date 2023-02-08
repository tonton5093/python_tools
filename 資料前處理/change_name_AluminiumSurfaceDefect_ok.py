import os
from shutil import copyfile
#path=input('請輸入資料夾：')
path = 'E:\\AluminiumSurfaceDefect\\Datasets\\Data\\POC001\\Image1\ok'
ok_path = 'E:\\AluminiumSurfaceDefect\\Datasets\\Data\\POC001\\Image1\\20180911_20180915'
dirs = os.listdir(path)#儲存所以資料夾內的檔案路徑

n = 1 #命名起始數字
file_type='jpg'
num = len(file_type)
for i in range(len(dirs)): 
    if(dirs[i][-num:]==file_type):       
        oldname=path+"\\"+dirs[i] #舊檔案的路徑
        
        new_dir_name = ok_path + "\\" + dirs[i][2:-8]
        os.makedirs(new_dir_name)#建立檔案
        print('建立檔案:',new_dir_name)
        new_file_path = new_dir_name  + '\\C1.' + file_type
        copyfile(oldname, new_file_path)#複製檔案(原始檔,目標檔案)
        print('copy:',new_file_path)