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

from func import *
from pyautogui import press
from pprint import pprint
from traceback import format_exc as msg_err
import os

In = []

_date_ = "2024 3.13"
_version_ = "1.20.4"
_active_ = True
_prompt_ = ""
_ErrorTries_ = 0
_KeyWord_ = "$"
_id_ = 0

def getData(fileObj):
    """获取JSON文件中的数据"""
    with open(fileObj, "r", encoding="utf-8") as file:
        data = load(file)
        return data

def main():
    print(
        f"""Clathon版本 {_version_}({_date_}) 64 Bits
Python规范版本:3.11.1 on Windows win32
    """
    )
    _line_ = 0
    while _active_:
        try:
            _prompt_ = f"In[{str(_line_).rjust(2)}] {os.getcwd()}>"
            _put_ = input(_prompt_)

            if _put_ == "exit" or _put_ == "quit":
                exit(0)
            elif _put_.startswith(_KeyWord_):
                os.system(_put_[1:])
                In.append(_put_)
                _line_ += 1
            elif _put_.startswith("?"):
                try:
                    if _put_.endswith(" "):
                        continue
                    print(get_help(eval(_put_[1:]), get=True))
                except SyntaxError:
                    print("?语法只支持变量,表达式和对象,而不是其他语句")
                In.append(_put_)
                _line_ += 1
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
                In.append(_put_)
                _line_ += 1
                exec(_block_code_)
            else:
                if (
                    _put_.startswith(" ") and _put_.endswith(" ")
                    ) or _put_ == "":
                    continue
                try:
                    _value_ = eval(_put_)
                    print(str(_value_))
                    del _value_
                    In.append(_put_)
                    _line_ += 1
                except SyntaxError:
                    try:
                        exec(_put_)
                        In.append(_put_)
                        _line_ += 1
                    except SyntaxError:
                        _error_ = msg_err().split("\n")
                        del _error_[:10]
                        del _error_[2]
                        In.append(_put_)
                        _line_ += 1
                        print("\n".join(_error_)[1:])
                    except Exception as _error_:
                        _error_ = msg_err().split("\n")
                        del _error_[1]
                        In.append(_put_)
                        _line_ += 1
                        print("\n".join(_error_))
                except Exception as _error_:
                    _error_ = msg_err().split("\n")
                    del _error_[1]
                    In.append(_put_)
                    _line_ += 1
                    print("\n".join(_error_))
                    In.append(_put_)
        except KeyboardInterrupt:
            cls()
        except Exception as _error_:
            _error_ = msg_err().split("\n")
            del _error_[1]
            In.append(_put_)
            _line_ += 1
            print("\n".join(_error_))

def run(files):
    try:
        for file in files:
            with open(file, "r", encoding="utf-8") as f:
                exec(f.read())
        exit()
    except Exception as error:
        print(str(error))
    else:
        pass

def shell(code="", In=In):
    try:
        _prompt_ = f"In [{str(_line_).rjust(2)}]>"
        _put_ = input(_prompt_)

        if _put_ == "exit" or _put_ == "quit":
            exit(0)
        elif _put_.startswith(_KeyWord_):
            os.system(_put_[1:])
            In.append(_put_)
            _line_ += 1
        elif _put_.startswith("?"):
            try:
                print(get_help(eval(_put_[1:]), get=True))
            except SyntaxError:
                print("?语法只支持变量,表达式和对象,而不是其他语句")
            In.append(_put_)
            _line_ += 1
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
            In.append(_put_)
            _line_ += 1
            exec(_block_code_)
        else:
            if (
                _put_.startswith(" ") and _put_.endswith(" ")
                ) or _put_ == "":
                return None
            try:
                _value_ = eval(_put_)
                print(str(_value_))
                del _value_
                In.append(_put_)
                _line_ += 1
            except SyntaxError:
                try:
                    exec(_put_)
                    In.append(_put_)
                    _line_ += 1
                except Exception as _error_:
                    _error_ = msg_err().split("\n")
                    del _error_[1]
                    In.append(_put_)
                    _line_ += 1
                    print("\n".join(_error_))
            except Exception as _error_:
                _error_ = msg_err().split("\n")
                del _error_[1]
                In.append(_put_)
                _line_ += 1
                print("\n".join(_error_))
                In.append(_put_)
    except KeyboardInterrupt:
        print("\n用户中断操作")
    except Exception as _error_:
        _error_ = msg_err().split("\n")
        del _error_[1]
        In.append(_put_)
        _line_ += 1
        print("\n".join(_error_))

if __name__ == "__main__":
    if len(argv) == 1:
        main()
    else:
        run(argv[1:])

