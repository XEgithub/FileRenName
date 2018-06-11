import os
path="." #定义当前路径
os.chdir(path) #跳转当前路径
for file in os.listdir(path):
    newfile=file.replace("*#dd","").replace("www","") #清除文件名中的符号
    os.rename(file,newfile) #修改文件名
    print(file+"------修改完成")    
