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
        import json
        import sys
        import os
        import random
        import time
        import datetime
        import threading

        def getData(fileObj):
            """获取JSON文件中的数据"""
            with open(fileObj, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data

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

        def about(returns=False):
            """显示Clathon的相关信息"""
            msg = f"""Clathon Version {_version_}({_date_})
Python�汾:Python 3.11.1 Windows
����:Hardy 2861205314@qq.com
Gitee:https://gitee.com/HardyProjects/clathon"""
            if not returns:
                return msg
            else:
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

            sys.setrecursionlimit(int(limit))
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
                text = json.dumps({"from": _id_, "text": text})
                f.write(text)

        # Systems
        def ___msg_system___():
            """监听目录下的clathon_message文件并将其信息打印至屏幕上"""
            import json

            while _active_:
                try:
                    with open("clathon_message", "r", encoding="utf-8") as f:
                        textObj = json.loads(f.read())
                        dtime = datetime.datetime.now().strftime("%H:%M:%S")
                        fid = textObj["from"]
                        text = textObj["text"]
                        _msg_dict_[dtime] = text
                        print(f"\n来自:{fid}")
                        print(f"信息:{text}\n")
                    os.system("del -r clathon_message")
                except FileNotFoundError:
                    pass
                time.sleep(0.1)

        def ___id_safe_system___():
            """保证_id_变量为常量,无法被修改"""
            global _id_
            backup_id = _id_
            while _active_:
                if _id_ != backup_id:
                    _id_ = backup_id

        ___IDSafeSystem___ = threading.Thread(target=___id_safe_system___)
        ___MessageSystem___ = threading.Thread(target=___msg_system___)
        ___IDSafeSystem___.start()
        ___MessageSystem___.start()

        for k, v in _configObj_.items():
            globals()[k] = v
        
        for num in range(IDRANGE):
            add = str(num * 2)
            IDLIST.append(add)
        _id_ = id(random.choice(IDLIST))
        del num, add, IDLIST, IDRANGE
        exec(_ConfigCode_)

        try:
            if len(sys.argv) >= 2:
                for file in sys.argv[1:]:
                    with open(file, "r", encoding="utf-8") as f:
                        exec(f.read())
                sys.exit()
            else:
                pass
        except Exception as error:
            print(str(error))
    except Exception as ErrorMessage:
        print(ErrorMessage)


def main():
    try:
        from pyautogui import press
        from pprint import pformat
        from traceback import format_exc as msg_err
    except ImportError:
        pass
    print(
        f"""Clathon Shell版本 {_version_}({_date_}) 64 Bits
Python规范版本:3.11.1
    """
    )
    _line_ = 0
    In = []
    while _active_:
        try:
            _prompt_ = f"In [{str(_line_).rjust(2)}]>"
            _put_ = input(_prompt_)
            _is_value_ = globals().get(_put_, False)

            try:
                eval(_put_)
            except SyntaxError:
                _v_ = False
            else:
                _is_value_ = eval(_put_)

            if _put_ == "exit" or _put_ == "quit":
                exit(0)
            elif _is_value_:
                _value_print_ = pformat(_is_value_)
                del _is_value_
                print(_value_print_)
                del _value_print_
            elif _put_.startswith(_KeyWord_):
                os.system(_put_[1:])
            elif _put_.startswith("?"):
                exec(f"help({_put_[1:]})")
            elif _put_.endswith(":"):
                _block_code_ = ""
                _block_code_ += _put_
                _block_active_ = True
                while _block_active_:
                    press("\t")
                    _block_put_ = input()
                    _block_code_ += "\n" + _block_put_
                    if (
                        _block_put_.startswith(" ") and _block_put_.endswith(" ")
                    ) or _block_put_ == "":
                        break
                exec(_block_code_)
            else:
                if (_put_.startswith(" ") and _put_.endswith(" ")) or _put_ == "":
                    continue
                exec(_put_)
            In.append(_put_)
        except Exception as _error_:
            _error_ = msg_err().split("\n")
            del _error_[1]
            In.append(_put_)
            _line_ += 1
            print("\n".join(_error_))

if __name__ == "__main__":
    main()