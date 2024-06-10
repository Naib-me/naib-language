import os
import sys
import tkinter as tk
from tkinter import messagebox

codefile = ""
codefileall = ""

def zhu (filePath):
    lines = 1
    run = open(f"{codefile}.rb",'w+',encoding="utf-8")
    run.write("# -*- coding: UTF-8 -*-\n")
    run.close()
    run = open(f"{codefile}.rb",'a',encoding="utf-8")
    with open(filePath, 'r', encoding='utf-8') as file:  # 确保使用正确的编码来支持中文
        for line in file:
            stripped_line = line.strip()  # 移除首尾空白字符
            if stripped_line:  # 检查是否为空行
                # 这里处理非空白行
                print(stripped_line)
                x = line.split(" ")
                if x[0] == "import":
                    if x[1] == "<my>":
                        modtxt = open(f"{os.getenv('APPDATA')}\\naib\\{x[2].split(" ")[0]}.rb","r",encoding="utf-8").read()
                        run.write(modtxt)
        lines += 1

if sys.argv[1] == "-v":
    print("naib Beta-0.20240610")
elif sys.argv[1] == "run":
    codefile = sys.argv[2].split(".")[0].split(" ")[0]
    codefileall = sys.argv[2].split(" ")[0]
    # 验证运行文件的后缀 == .naib
    if sys.argv[2].split(".")[1].split(" ")[0] == "naib":
        print("后缀验证 OK")
        zhu(codefileall)
    else:
        messagebox.showinfo("提示", "你的文件后缀输入错误!")
        
        
