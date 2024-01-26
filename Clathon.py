# -- coding: utf-8 --**
"""Clathon is a Python interpreter written in CPython. \
There are a lot of functions added to it (i.e. writing \
a Python in Python, and I was blown away by the implementation)
Setup and Usage:
Before using it,Don't forget to add the Clathon installation directory to PATH!
Once set up, you can use the clathon command to open the \
Clathon interactive environment, or run the file with the clathon <file>
The URL of the Gitee project repository: https://gitee.com/HardyProjects/clathon
Repository address: git@gitee.com: HardyProjects/clathon.git
Author: Cyan Wolf
Date: 2024/1/1
Version: 1.20.2
Description: Clathon is a Python interpreter written in CPython.
"""

# Code Specification:
# 1. All code must be written in the Python 3.11.10 standard.
# 2. All code must be written in the UTF-8 encoding.
# 3. The one that starts with "_" is an internal variable (non-constant).
# 4. Threads that start with "___".
# Preparation
for i in range(1):
    try:
        import json
        import sys
        import os
        import random
        import time
        import datetime
        import threading

        def run(fileObj, comment=False, out=False):
            """Run a Python file."""
            file = open(fileObj, "r", encoding="utf-8")
            code = file.read()
            if comment:
                print(f"======= File {str(fileObj)} is running =======")
            else:
                pass
            if out:
                return code
            else:
                exec(code)

        def getData(fileObj):
            """Get data from a JSON file."""
            with open(fileObj, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data

        # Values
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
        _date_ = "2024 New Year"
        _version_ = "1.20.2"
        _id_ = 0

        # Functions
        def about(returns=False):
            """Display information about Clathon"""
            msg = f"""Clathon Version {_version_}({_date_})
Work And Edit with : Python 3.11.1 Windows
Author : Hardy 2861205314@qq.com
Gitee:https://gitee.com/HardyProjects/clathon"""
            if not returns:
                return msg
            else:
                print(msg)

        # class Requirements:
        #     """Requirements for Clathon"""

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
            """Change work directory to <path>"""
            os.chdir(path)

        def cls():
            """Clear the terminal screen"""
            os.system("cls")

        def exit(status_code=0):
            """Exit Clathon
            Alias of quit()"""
            os._exit(status_code)

        def quit(status_code=0):
            """Exit Clathon
            Alias of exit()"""
            os._exit(status_code)

        def crash(limit=9999999):
            """Crash the Clathon"""

            def stack():
                stack()

            sys.setrecursionlimit(int(limit))
            stack()

        def ifType(aObj, bObj):
            """Check if aObj is type of bObj"""
            return type(aObj) == type(bObj)

        def load(symbol="-", times=10):
            """Loading a moment"""
            for i in range(times):
                for j in range(4):
                    print("Loading" + f"{'.' * i}")
                    print(f"{symbol * i}")
                    time.sleep(0.5)
                    cls()

        def lock():
            """Lock a moment until user press Ctrl+C"""
            while True:
                try:
                    cls()
                except KeyboardInterrupt:
                    break

        def title(text):
            """Set the terminal title"""
            os.system(f"title {text}")

        def send(text=""):
            """Send message"""
            with open("clathon_message", "w", encoding="utf-8") as f:
                text = json.dumps({"from": _id_, "text": text})
                f.write(text)

        # Systems
        def ___msg_system___():
            """Message systemListen to the message file \
            and send it to the corresponding function"""
            import json

            while _active_:
                try:
                    with open("clathon_message", "r", encoding="utf-8") as f:
                        textObj = json.loads(f.read())
                        dtime = datetime.datetime.now().strftime("%H:%M:%S")
                        fid = textObj["from"]
                        text = textObj["text"]
                        _msg_dict_[dtime] = text
                        print(f"\nFrom:{fid}")
                        print(f"Text:{text}\n")
                    os.system("del -r clathon_message")
                except FileNotFoundError:
                    pass
                time.sleep(0.1)

        def ___id_safe_system___():
            """Id safe system
This system is used to prevent the id from changing while \
the program is running."""
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
        
        # Run files
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
        f"""Clathon Version {_version_}({_date_}) 64 Bits
Python Version 3.11.1 Windows
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
        except KeyboardInterrupt:
            print("User Interrupted")
        except Exception as _error_:
            _error_ = msg_err().split("\n")
            del _error_[1]
            In.append(_put_)
            _line_ += 1
            print("\n".join(_error_))

if __name__ == "__main__":
    main()