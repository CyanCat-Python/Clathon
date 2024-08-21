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
日期:2024/8/21
版本: 1.20.8
描述:Clathon 是用 CPython 编写的 Python 解释器。
"""

from func import *
from func import _version_, _date_, _active_, _KeyWord_, _prompt_
from pyautogui import press
from pprint import pprint
from traceback import format_exc as msg_err
import pickle
import os

In = []

def main():
    """Clathon Shell的主入口函数"""
    global _version_, _prompt_, _active_, _date_, _KeyWord_
    info(
        f"""Clathon版本 {_version_}({_date_}) 64 Bits
Python规范版本:3.11.1 on Windows win32
    """
    )
    _line_ = 0
    _put_ = ""
    while _active_:
        try:
            _put_ = input(eval(_prompt_))

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
                    info(get_help(eval(_put_[1:]), get=True))
                except SyntaxError:
                    error("?语法只支持变量,表达式和对象,而不是其他语句")
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
                    user(str(_value_))
                    del _value_
                    In.append(_put_)
                    _line_ += 1
                except SyntaxError:
                    try:
                        exec(_put_)
                        In.append(_put_)
                        _line_ += 1
                    except SyntaxError:
                        try:
                            for char in """`~!@#$%^&*_+-={}[];:'\"|\\,<.>/?""":
                                if char not in _put_.split(" ")[0]:
                                    if callable(eval(_put_.split(" ")[0])):
                                        exec(f"{_put_.split(' ')[0]}({','.join(_put_.split(' ')[1:])})")
                                        In.append(_put_)
                                        _line_ += 1
                                        break
                            del char
                        except SyntaxError:
                            _error_ = msg_err().split("\n")
                            del _error_[:10]
                            del _error_[2]
                            In.append(_put_)
                            _line_ += 1
                            error("\n".join(_error_)[1:])
                        except Exception as _error_:
                            _error_ = msg_err().split("\n")
                            del _error_[:10]
                            del _error_[2]
                            In.append(_put_)
                            _line_ += 1
                            error("\n".join(_error_)[1:])
                    except Exception as _error_:
                        _error_ = msg_err().split("\n")
                        del _error_[1]
                        In.append(_put_)
                        _line_ += 1
                        error("\n".join(_error_))
                except Exception as _error_:
                    _error_ = msg_err().split("\n")
                    del _error_[1]
                    In.append(_put_)
                    _line_ += 1
                    error("\n".join(_error_))
                    In.append(_put_)
        except KeyboardInterrupt:
            cls()
        except EOFError:
            exit(0)
        except Exception as _error_:
            _error_ = msg_err().split("\n")
            del _error_[1]
            In.append(_put_)
            _line_ += 1
            error("\n".join(_error_))

def shell(code="", In=In):
    """用于在文件中模拟Clathon Shell的运行结果"""
    global get_help
    _line_ = 0
    try:
        _put_ = code
        if _put_ == "exit" or _put_ == "quit":
            exit(0)
        elif _put_.startswith(_KeyWord_):
            os.system(_put_[1:])
            In.append(_put_)
            _line_ += 1
        elif _put_.startswith("?"):
            try:
                if _put_.endswith(" "):
                    return None
                info(get_help(eval(_put_[1:]), get=True))
            except SyntaxError:
                error("?语法只支持变量,表达式和对象,而不是其他语句")
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
                user(str(_value_))
                del _value_
                In.append(_put_)
                _line_ += 1
            except SyntaxError:
                try:
                    exec(_put_)
                    In.append(_put_)
                    _line_ += 1
                except SyntaxError:
                    try:
                        for char in """`~!@#$%^&*_+-={}[];:'\"|\\,<.>/?""":
                            if char not in _put_.split(" ")[0]:
                                if callable(eval(_put_.split(" ")[0])):
                                    exec(f"{_put_.split(' ')[0]}({','.join(_put_.split(' ')[1:])})")
                                    In.append(_put_)
                                    _line_ += 1
                                    break
                        del char
                    except SyntaxError:
                        _error_ = msg_err().split("\n")
                        del _error_[:10]
                        del _error_[2]
                        In.append(_put_)
                        _line_ += 1
                        error("\n".join(_error_)[1:])
                    except Exception as _error_:
                        _error_ = msg_err().split("\n")
                        del _error_[:10]
                        del _error_[2]
                        In.append(_put_)
                        _line_ += 1
                        error("\n".join(_error_)[1:])
                except Exception as _error_:
                    _error_ = msg_err().split("\n")
                    del _error_[1]
                    In.append(_put_)
                    _line_ += 1
                    error("\n".join(_error_))
            except Exception as _error_:
                _error_ = msg_err().split("\n")
                del _error_[1]
                In.append(_put_)
                _line_ += 1
                error("\n".join(_error_))
                In.append(_put_)
    except KeyboardInterrupt:
        cls()
    except EOFError:
        exit(0)
    except Exception as _error_:
        _error_ = msg_err().split("\n")
        del _error_[1]
        In.append(_put_)
        _line_ += 1
        error("\n".join(_error_))

def run(files, shell_mode=False):
    try:
        for file in files:
            with open(file, "r", encoding="utf-8") as f:
                if shell_mode:
                    for line in f.read().splitlines():
                        shell(code=line)
                else:
                    exec(f.read())
        exit()
    except Exception as error:
        _error_ = msg_err().split("\n")
        del _error_[1]
        error("\n".join(_error_))
    else:
        pass

def arg_main(args=argv):
    if len(argv) == 1:
        main()
    else:
        if not argv[1].startswith("-"):
            run(argv[1:])
        else:
            argv[1] = argv[1].lower()
            if argv[1] == "-s" or argv[1] == "--shell":
                run(argv[2:], shell_mode=True)
            elif argv[1] == "-v" or argv[1] == "--verison":
                info("Clathon版本:" + _version_)
                info("最后更新日期:" + _date_)
                info("GNU LGPL v3")
            elif argv[1] == "-l" or argv[1] == "--line":
                exec(" ".join(argv[2:]))
            elif argv[1] == "-d" or argv[1] == "--dir":
                cd(" ".join(argv[2:]))
                main()
            elif argv[1] == "-i" or argv[1] == "--import":
                for module in argv[2:]:
                    exec("import " + module)
                main()
            elif argv[1] == "-c" or argv[1] == "--complie":
                if len(argv) < 4:
                    error("缺少参数: <output-file>")
                    info("用法:")
                    info("  clathon -c <input-file> <output-file>")
                else:
                    with open(argv[2], "r", encoding="utf-8") as put_file:
                        with open(argv[3], "wb") as out_file:
                            pickle.dump(put_file.read(), out_file, 2)
            elif argv[1] == "-y" or argv[1] == "--spy":
                if len(argv) < 3:
                    error("缺少参数: <input-file>")
                    info("用法:")
                    info("  clathon -y <input-file>")
                else:
                    try:
                        with open(argv[2], "rb") as put_file:
                            exec(pickle.load(put_file))
                    except FileNotFoundError:
                        error(f"{argv[2]}文件未找到")
                    except:
                        _error_ = msg_err().split("\n")
                        del _error_[1]
                        error("\n".join(_error_))
            elif argv[1] == "-h" or argv[1] == "--help" or argv[1] == "-?":
                info("用法Usage:")
                info("-s/--shell 运行文件模拟在Shell中")
                info("-v/--version 显示Clathon版本")
                info("-l/--line 快捷运行单行代码")
                info("-h/--help/-? 显示此帮助消息")
                info("-d/--dir 指定Clathon Shell打开的路径")
                info("-i/--import 指定Clathon Shell打开时导入的库")
                #info("-g/--config 指定Clathon Shell打开时运行的config")
                info("-y/--pys 运行SPY文件")
                info("-c/--complie 编译Clathon文件为SPY")
                #info("-m/--module 运行/编译PYC文件")

if __name__ == "__main__":
    arg_main()