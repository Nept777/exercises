import os
import shutil

def traverse_folder(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            splits = dirpath.split('\\')
            to_path = splits[0] + '\\' + splits[1] + '\\' + splits[2] + '\\' + splits[3] + '\\' + filename
            print(to_path)
            shutil.move(file_path,to_path)
            # 处理文件操作



# 调用示例
traverse_folder('Z:\\媒体库\\BYK\\KZ')