import os
import shutil


# 将指定文件夹中的下级文件移动到上一级

def traverse_folder(path, step):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            last_split_index = file_path.rfind('\\', 0, len(file_path))
            to_path_left = file_path[0:last_split_index]
            # 根据step返回正确的反斜杠下标
            for i in range(0, step):
                cir_last_split_index = to_path_left.rfind('\\', 0, len(to_path_left))
                to_path_left = file_path[0:cir_last_split_index]

            to_path = to_path_left + '\\' + filename
            print(to_path)
            shutil.move(file_path, to_path)
            # 处理文件操作


# 调用示例

traverse_folder('Z:\\媒体库\\ASMR\\梵拉', 1)
