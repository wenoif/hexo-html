#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import time

def Rename(path):
    for root, dirs, files in os.walk(path, topdown=True):
        """
        print("\nroot:")
        print(root)
        print("\ndirs:")
        print(dirs)
        print("\nfiles:")
        print(files)
        """
        for file_name in files:
            file_name_split=file_name.split('.')
            # 拆分文件名
            # print(file_name_split)
            try:
                if file_name_split[-1] == 'md':
                    open_file_path = os.path.join(root,file_name)
                    # 拼接文件路径
                    # print(open_file_path)

                    with open(open_file_path,'r',encoding='utf8') as fr:
                        text=fr.read()
                        # 提取文件内容
                        # print(type(text))

                        title = re.findall("title: (.*)\nid",text);
                        blogid = re.findall("id: (.*)\ndate",text);
                        date = re.findall("date: (.*) .{5,8}\ncategories",text)
                        # 提取指定字符
                        # print(title)
                        # print(blogid)
                        # print(date)
                    new_file_name=''.join(date) + '@' + ''.join(blogid) + '@' + ''.join(title) + '.md'
                    # 重组新的文件名
                    # print(new_file_name)
                    # print(type(new_file_name))

                    new_file_path = os.path.join(root,new_file_name)
                    # 重组新的路径
                    # print(new_file_path)
                    print("检查中，请稍等......")
                    if( open_file_path != new_file_path):
                        os.rename(open_file_path,new_file_path)
                        # 修改文件名
                        print(f'{file_name} --> {new_file_name} ....OK');
                        # time.sleep(0.01)
            except FileNotFoundError as e:
                print(e)
            #time.sleep(0.2)



if __name__=='__main__':
    path=r'../_posts/'
    # 'r'是防止字符转义的 如果路径中出现'\t'的话 不加r的话\t就会被转义 而加了'r'之后'\t'就能保留原有的样子
    Rename(path)
    # 将文件名改成“时间-标题@id.md”的格式，例如：“2020-10-15-电@electrical.md”
    print("修改完毕")
