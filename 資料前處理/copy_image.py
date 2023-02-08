import os
from shutil import copyfile
#path=input('請輸入資料夾：')
path = 'E:\\spindle\\Datasets\\Data\\NOGV0A1301\\Image2\\20230204'
save_path = 'D:\\code\\python_tools\\copy_images'
dirs = os.listdir(path)#儲存所以資料夾內的檔案路徑

for i in range(len(dirs)):       
    image_path = os.path.join(path,dirs[i],'Y4_X1.bmp') #舊檔案的路徑
    new_image_name = dirs[i]+".jpg"
    new_image_name_path = os.path.join(save_path,new_image_name)
    print('copyfile:',new_image_name_path)
    copyfile(image_path, new_image_name_path)#複製檔案(原始檔,目標檔案)