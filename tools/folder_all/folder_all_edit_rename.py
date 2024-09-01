import os
import shutil


# 将指定文件夹中的下级文件移动到指定文件夹

# 遍历路径下所有文件和文件夹
def traverse_folder_all(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)

            # 处理filename

            # 删除指定字符串
            # 截取指定长度
            filename = filename.replace("hhd800.com@", "")

            # 添加前缀
            # 添加后缀

            to_path = path + '\\' + filename
            print(to_path)
            shutil.move(file_path, to_path)
            # 处理文件操作

# 调用示例
# traverse_folder_all('Z:\\媒体库\\BYK\\KZ\\口罩姬2')
traverse_folder_all('Z:\\媒体库\\BYK\\KZ')
