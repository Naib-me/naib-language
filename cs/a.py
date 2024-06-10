import os

x = "io"
print(open(f"{os.getenv('APPDATA')}\\naib\\{x.split(" ")[0]}.rb","r",encoding="utf-8").read())