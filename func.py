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

for i in range(1):
    try:
        from json import load, loads, dump, dumps
        from sys import argv, setrecursionlimit, exit
        import os
        from time import sleep
        from random import choice
        from datetime import datetime
        from threading import Thread

        def getData(fileObj):
            """获取JSON文件中的数据"""
            with open(fileObj, "r", encoding="utf-8") as file:
                data = load(file)
                return data

        def get_help(codeObj, get=False):
            """用于获取对象(codeObj)的帮助"""
            data = str(codeObj)
            typeObj = str(type(codeObj))
            doc = codeObj.__doc__
            msg = f"""数据:{data}
类型:{typeObj}
文档:{doc}
"""
            if get:
                return msg
            else:
                print(msg)

        _prompt_ = ""
        _put_ = ""
        IDRANGE, IDLIST = 5, []
        _active_ = True
        _configObj_ = getData(os.environ["USERPROFILE"] + "\\config.json")
        _config_path_ = _configObj_["config_path"]
        _ErrorTries_ = 0
        _msg_dict_ = {}
        _KeyWord_ = "$"
        _ConfigCode_ = ""
        with open(_config_path_, "r", encoding="utf-8") as f:
            _ConfigCode_ = f.read()
        del f
        _date_ = "2024 1.26"
        _version_ = "1.20.4"
        _id_ = 0

        def about():
            """显示Clathon的相关信息"""
            msg = f"""Clathon Version {_version_}({_date_})
Python版本:Python 3.11.1 Windows
作者:Hardy 2861205314@qq.com
Gitee地址:https://gitee.com/HardyProjects/clathon"""
            print(msg)

        # class Requirements:
        #     """cx-freeze打包时一同打包的库
        #        仅在cx-freeze打包时启用,使用Pyinstaller打包时请将其注释掉"""
        #     def __init__(self):
        #         import pyforest
        #         import math
        #         import re
        #         import requests
        #         import random
        #         import os
        #         import time
        #         import sys
        #         import datetime
        #         import json
        #         import hashlib
        #         import base64
        #         import subprocess
        #         import threading
        #         import urllib.request
        #         import urllib.parse
        #         import urllib.error
        #         import http.client
        #         import http.server
        #         import socketserver
        #         import socket
        #         import tkinter
        #         import tkinter.messagebox
        #         import tkinter.filedialog
        #         import tkinter.simpledialog
        #         import tkinter.colorchooser
        #         import tkinter.ttk
        #         import tkinter.constants
        #         import tkinter.dnd
        #         import tkinter.scrolledtext
        #         import tkinter.font
        #         import pyautogui
        #         import PIL
        #         import pathlib
        #         from pathlib import Path

        def cd(path):
            """更改工作目录至<path>参数"""
            os.chdir(path)

        def cls():
            """清空终端"""
            os.system("cls")

        def exit(status_code=0):
            """退出"""
            os._exit(status_code)

        def quit(status_code=0):
            """退出"""
            os._exit(status_code)

        def crash(limit=9999999):
            """使用栈溢出引发人为崩溃(非必要不要使用!)"""

            def stack():
                stack()

            setrecursionlimit(int(limit))
            stack()

        def ifType(aObj, bObj):
            """检查a的类型是b的类型"""
            return type(aObj) == type(bObj)

        def title(text):
            """设置终端的标题"""
            os.system(f"title {text}")

        def send(text=""):
            """发送消息(依赖msg_system)"""
            with open("clathon_message", "w", encoding="utf-8") as f:
                text = dumps({"from": _id_, "text": text})
                f.write(text)
        
        for k, v in _configObj_.items():
            globals()[k] = v

        for num in range(IDRANGE):
            add = str(num * 2)
            IDLIST.append(add)
        _id_ = id(choice(IDLIST))

        del num, add, IDLIST, IDRANGE, k, v
        exec(_ConfigCode_)

    except Exception as ErrorMessage:
        print(ErrorMessage)