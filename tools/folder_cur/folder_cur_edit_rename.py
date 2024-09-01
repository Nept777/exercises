import os
import shutil


# 将指定文件夹中的下级文件移动到指定文件夹

# 遍历当前文件夹所有文件
def traverse_folder_cur(path):
    file_list = os.listdir(path)  # 获取当前文件夹中的文件列表
    for filename_org in file_list:

        # 处理filename
        # 删除指定字符串
        # 截取指定长度
        filename = filename_org.replace("pdf", "mp4")

        # 添加前缀
        # 添加后缀

        org_path = path + '\\' + filename_org
        if os.path.isdir(org_path):
            continue
        to_path = path + '\\' + filename
        print(to_path)
        shutil.move(org_path, to_path)
        # 处理文件操作

# 调用示例
traverse_folder_cur('Z:\\媒体库\\影视\\躺柜1')
