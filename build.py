import os
import shutil

# 创建文件夹
os.makedirs(f"{os.getenv('APPDATA')}\\naib", exist_ok=True) 
# 源文件路径
src = './script/io.rb'
# 目标文件路径
dst = f"{os.getenv('APPDATA')}\\naib"

# 复制文件
shutil.copy(src, dst)