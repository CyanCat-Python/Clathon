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

from func import _active_, loads, datetime, _msg_dict_, os, sleep, Thread

for i in range(1):
    try:
        # Systems
        def ___msg_system___():
            """监听工作目录下的clathon_message文件并将其信息打印至屏幕上"""
            while _active_:
                try:
                    with open("clathon_message", "r", encoding="utf-8") as f:
                        textObj = loads(f.read())
                        dtime = datetime.datetime.now().strftime("%H:%M:%S")
                        fid = textObj["from"]
                        text = textObj["text"]
                        _msg_dict_[dtime] = text
                        print(f"\n来自:{fid}")
                        print(f"信息:{text}\n")
                    os.system("del -r clathon_message")
                except FileNotFoundError:
                    pass
                sleep(0.1)

        def ___id_safe_system___():
            """保证设置的变量为常量,无法被修改"""
            global _id_
            backup_id = _id_
            while _active_:
                if _id_ != backup_id:
                    _id_ = backup_id
        
        def ___clear_system___():
            import keyboard as key
            global cls
            while _active_:
                key.add_hotkey("pause", target=cls)
                key.wait()

        ___IDSafeSystem___ = Thread(target=___id_safe_system___)
        ___MessageSystem___ = Thread(target=___msg_system___)

        ___IDSafeSystem___.start()
        ___MessageSystem___.start()
    except Exception as error:
        print(error)