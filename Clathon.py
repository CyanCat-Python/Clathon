# -- coding: utf-8 --**
"""Clathon 是一个用 CPython 编写的 Python 解释器。它添加了很多功能(即编写
Python 中的 Python，我被实现震撼了)
设置和使用:
使用前，别忘了将Clathon安装目录添加到PATH中!
设置完成后，您可以使用 clathon 命令打开
Clathon 交互式环境，或使用 clathon <file>运行文件
Gitee 项目仓库的 URL:https://gitee.com/HardyProjects/clathon
仓库地址:git@gitee.com:HardyProjects/clathon.git
作者： Cyan Wolf
日期:2024/1/1
版本: 1.20.4
描述:Clathon 是用 CPython 编写的 Python 解释器。
"""
from shell import *
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        main()
    else:
        run(argv[1:])
