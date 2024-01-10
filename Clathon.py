# -- coding: utf-8 --**
"""Clathon is a Python interpreter written in CPython. There are a lot of functions added to it (i.e. writing a Python in Python, and I was blown away by the implementation)
Setup and Usage:
Before using it,Don't forget to add the Clathon installation directory to PATH!
Once set up, you can use the clathon command to open the Clathon interactive environment, or run the file with the clathon <file>
The URL of the Gitee project repository: https://gitee.com/MinePy/clathon
Repository address: git@gitee.com: MinePy/clathon.git
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
        from pathlib import Path
        import sys
        import os
        import turtle, random
        import time, datetime
        import threading

        def run(fileObj, comment=False, out=False):
            """Run a Python file."""
            file = open(fileObj, "r", encoding="utf-8")
            code = file.read()
            if comment:
                print(f"=======File {str(fileObj)} is running=======")
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
        _prompt_ = "Command>>"
        _put_ = ""
        IDRANGE, IDLIST = 999, []
        _active_ = True
        _configObj_ = getData(
            os.environ["USERPROFILE"] + "\\config.json"
        )
        _config_path_ = _configObj_["config_path"]
        _ErrorTries_ = 0
        _msg_dict_ = {}
        _KeyWord_ = "$"
        _ConfigCode_ = ""
        with open(_config_path_, "r", encoding="utf-8") as f:
            _ConfigCode_ = f.read()
        del f
        exec(_ConfigCode_)
        _date_ = "2024 New Year"
        _version_ = "1.20.2"
        _id_ = 0
        for num in range(IDRANGE):
            add = str(num * 2)
            IDLIST.append(add)
        _id_ = id(random.choice(IDLIST))
        del num, add, IDLIST, IDRANGE

        # Functions
        def about(returns=False):
            """Display information about Clathon"""
            msg = f"""Clathon Version {_version_}({_date_})
Work And Edit with : Python 3.11.1 Windows
Author : Hardy 2861205314@qq.com
Gitee:https://gitee.com/MinePy/clathon"""
            if not returns:
                return msg
            else:
                print(msg)

        class Requirements:
            """Requirements for Clathon"""
            def __init__(self):
                import pyforest
                import math
                import re
                import requests
                import random
                import os
                import time
                import sys
                import datetime
                import json
                import hashlib
                import base64
                import subprocess
                import threading
                import urllib.request
                import urllib.parse
                import urllib.error
                import http.client
                import http.server
                import socketserver
                import socket
                import tkinter
                import tkinter.messagebox
                import tkinter.filedialog
                import tkinter.simpledialog
                import tkinter.colorchooser
                import tkinter.ttk
                import tkinter.constants
                import tkinter.dnd
                import tkinter.scrolledtext
                import tkinter.font
                import pyautogui
                import PIL
                import pathlib
                from pathlib import Path

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

        def enter_code():
            """Enter code"""
            code = easygui.codebox(msg="Enter your code", title="Clathon CodeBox")
            if code.isspace():
                return None
            else:
                exec(code)

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
                except:
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
            """Message systemListen to the message file and send it to the corresponding function"""
            import json

            while _active_:
                try:
                    with open("clathon_message", "r", encoding="utf-8") as f:
                        textObj = json.loads(f.read())
                        dtime = datetime.datetime.now().strftime("%H:%M:%S")# %Y/%m/%d
                        fid = textObj["from"]
                        text = textObj["text"]
                        _msg_dict_[dtime] = text
                        print(f"\nFrom:{fid}")
                        print(f"Text:{text}\n")
                    os.system("del -r clathon_message")
                except:
                    pass
                time.sleep(0.1)

        def ___id_safe_system___():
            """Id safe system
This system is used to prevent the id from changing while the program is running."""
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
            import traceback

            print(str(error))
    except Exception as ErrorMessage:
        print(ErrorMessage)

if __name__ == "__main__":
    # Import modules
    try:
        import easygui, pprint
        import traceback
    except:
        pass
    print(
        f"""Clathon Version {_version_}({_date_}) 64 Bits
Python Version 3.11.1 Windows
    """
    )
    while _active_:
        try:
            _put_ = input(_prompt_)
            _is_value_ = globals().get(_put_, False)
            if _put_ == "exit" or _put_ == "quit":
                exit(0)
            elif _is_value_:
                _value_print_ = pprint.pformat(globals()[_put_])
                print(_value_print_)
            elif _put_.startswith(_KeyWord_):
                os.system(_put_[1:])
            elif _put_.endswith(":"):
                _block_code_ = ""
                _block_code_ += _put_
                _block_active_ = True
                while _block_active_:
                    _block_put_ = input()
                    _block_code_ += "\n" + _block_put_
                    if (_block_put_.startswith(' ') and _block_put_.endswith(' ')) or _block_put_ == "":
                        break
                exec(_block_code_)
            else:
                exec(_put_)
        except KeyboardInterrupt:
            cls()
        except:
            _error_ = traceback.format_exc().split("\n")
            del _error_[1]
            print("\n".join(_error_))
