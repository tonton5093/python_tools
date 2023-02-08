import os
from shutil import copyfile
import numpy as np
#path=input('請輸入資料夾：')
path = 'E:\\AluminiumSurfaceDefect\\Datasets\\Data\\POC001\\Image2\\ng'
ng_path = 'E:\\AluminiumSurfaceDefect\\Datasets\\Data\\POC001\\Image2\\20180911_20180915'
dirs = os.listdir(path)#儲存所以資料夾內的檔案路徑ex.C:\Users\USER\Desktop\HW1\附檔\1.txt

def selectRandom(names):
  return np.random.choice(names, 5, False)


def copy_imgae(dir_path,images):
    
    for i in range(len(images)):
        if(images[i][-num:]==file_type):       
            oldname = os.path.join(dir_path,images[i])#舊檔案的路徑  
            new_dir_name = ng_path + "\\" + images[i][-22:-8]
            os.makedirs(new_dir_name)#建立檔案
            print('建立檔案:',new_dir_name)
            new_file_path = new_dir_name  + '\\C1.' + file_type
            copyfile(oldname, new_file_path)#複製檔案(原始檔,目標檔案)
            print('copy:',new_file_path)   
            
if __name__ == '__main__':  
    
    file_type='jpg'
    num = len(file_type)
    
    for dir_name in dirs :
        if dir_name != '其他':
            pass
            print(dir_name)
            images = os.listdir(os.path.join(path, dir_name))
            np.random.seed(1)
            images = selectRandom(images)
            dir_path =  os.path.join(path, dir_name)
            copy_imgae(dir_path,images)
        else:
            other_dirs_names = os.listdir(os.path.join(path, dir_name))
            for other_dir in other_dirs_names:#取得其他資料夾內，資料夾名稱
                print(other_dir)
                other_dirs_paths = os.path.join(path, dir_name,other_dir)
                if(os.path.isdir(other_dirs_paths)):#判斷是否為資料夾，排除.DS_Store 
                    images = os.listdir(other_dirs_paths)                 
                    images = [value for value in images if value[-num:] == file_type]#排除不是jpg的檔案
                    np.random.seed(1)
                    if len(images) >5:
                        images = selectRandom(images)
                    dir_path = other_dirs_paths
                    copy_imgae(dir_path,images)           