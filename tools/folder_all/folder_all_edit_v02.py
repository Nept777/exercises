import os
import shutil


# 将path中的所有下级文件移动到path

def traverse_folder(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            to_path = path + '\\' + filename
            print(to_path)
            shutil.move(file_path, to_path)
            # 处理文件操作


# 调用示例
traverse_folder('Z:\\媒体库\\ASMR\\梵拉')
