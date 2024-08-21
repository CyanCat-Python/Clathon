"""Clathon 是一个用 CPython 编写的 Python 解释器。它添加了很多功能(即编写
Python 中的 Python，我被实现震撼了)
设置和使用:
使用前，别忘了将Clathon安装目录添加到PATH中!
设置完成后，您可以使用 clathon 命令打开
Clathon 交互式环境，或使用 clathon <file>运行文件
Gitee 项目仓库的 URL:https://gitee.com/HardyProjects/clathon
仓库地址:git@gitee.com:HardyProjects/clathon.git
作者： Cyan Wolf
日期:2024/8/18
版本: 1.20.7
描述:Clathon 是用 CPython 编写的 Python 解释器。
"""

from termcolor import colored

def getData(fileObj):
    """获取JSON文件中的数据"""
    with open(fileObj, "r", encoding="utf-8") as file:
        data = load(file)
        return data


for i in range(1):
    try:
        from json import load, loads, dump, dumps
        from sys import argv, setrecursionlimit, exit
        import os
        from time import sleep
        from random import choice
        from datetime import datetime
        from threading import Thread

        _configObj_ = getData(os.environ["USERPROFILE"] + "\\config.json")
        _config_path_ = _configObj_["config_path"]
        _ConfigCode_ = ""
        _date_ = "2024 8.18"
        _version_ = "1.20.7"
        _active_ = True
        _KeyWord_ = "$"
        _prompt_ = 'colored(f"In[{str(_line_).rjust(2)}] >", "green")'

        def info(text, end="\n"):
            print(colored(text, "yellow"), end=end)

        def text(text, end="\n"):
            print(colored(text, "white"), end=end)

        def user(text, end="\n"):
            print(colored(text, "magenta"), end=end)

        def error(text, end="\n"):
            print(colored(text, "red"), end=end)


        def str_ord(string):
            """把string中的所有字符转为Unicode字符值再返回"""
            result = [ord(char) for char in string]
            return result
            
        def list_chr(the_list):
            """把the_list中的所有元素当成Unicode字符值转为string"""
            result = ""
            for orded_char in the_list:
                result += chr(orded_char)
            return result

        def crash(limit=999999999, cancel=True):
            import sys, time
            sys.setrecursionlimit(limit)
            if True:
                error("警告Warning:此操作可能会导致当前调用此函数的 \
Clathon会话(Shell/File)崩溃, 严重时系统将卡死, 未保存的进度和工作将丢失 \
若并非本人操作, 请取消. (YES/no)")
                warning_put = input()
                if warning_put == "YES":
                    pass
                else:
                    return None
            def stack():
                stack()
            try:
                stack()
            except RecursionError:
                    info("此崩溃操作未成功, limit参数至少为1000")
            return
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

        with open(_config_path_, "r", encoding="utf-8") as f:
            _ConfigCode_ = f.read()
        del f

        def about():
            """显示Clathon的相关信息"""
            msg = f"""Clathon Version {_version_}({_date_})
Python版本:Python 3.11.1 Windows
作者:Hardy 2861205314@qq.com
Gitee地址:https://gitee.com/HardyProjects/clathon"""
            print(msg)

        # class Requirements:
        #     """cx-freeze打包时一同打包的库
        #        仅在cx-freeze打包时启用(用于将以下库一同打包),使用Pyinstaller打包时请将其注释掉"""
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
            try:
                os.system("cls")
            except:
                pass

        def exit(status_code=0):
            """退出"""
            os._exit(status_code)

        def quit(status_code=0):
            """退出"""
            os._exit(status_code)

        def ifType(aObj, bObj):
            """检查a的类型是b的类型"""
            return type(aObj) == type(bObj)

        def title(text):
            """设置终端的标题"""
            os.system(f"title {text}")
        
        for k, v in _configObj_.items():
            globals()[k] = v
        
        del k, v

        exec(_ConfigCode_)

    except Exception as _ErrorMessage_:
        print("配置文件出现问题:", end="")
        print(_ErrorMessage_)

del i