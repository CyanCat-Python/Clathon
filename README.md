# **Clathon                                                                           [![Fork me on Gitee](https://gitee.com/HardyProjects/clathon/widgets/widget_3.svg)](https://gitee.com/HardyProjects/clathon)**

## 介绍

用CPython来实现Python规范，一个用Python写的Python

你可以把它的EXE版本作为一个Python解释器，如果你安装了它的源码版本，则可以把它作为一个加强PythonShell

功能包括：

* 通过用户目录下的config.json指定config.py（Clathon启动时自动运行的脚本），同时也可以用config.json定义简单的数据、变量。
* 加强的 Shell功能：
  * 快捷函数调用：

    ```
    In[0]>print("Hello")
    Hello
    In[1]>print "Hello"
    Hello
    In[2]>input Prompt:
    Prompt:For Example
    For Example
    ```
  * Ctrl+C快捷中断清屏：
    ```
    In[0]>^C
    (Clear Screen)
    In[0]>_
    ```
  * 快捷运行系统Shell：

    ```
    In[0]>#System for example is Windows 
    In[1]>$pwd
    C:\Users\Example
    In[2]>$echo Hello, world
    Hello, world
    ```
  * 模拟ClathonShell运行：

    ```
    In[0]>#Clathon Shell
    In[1]>print
    <built-in function print>
    In[2]>shell("print")
    <built-in function print>
    ```

    ```
      1 #File example1.py
      2 shell("print")
    ```

    ```
      1 #File example2.py
      2 print
    ```

    ```
    C:\Users\Example\>clathon example1.py
    <built-in function print>
    C:\Users\Example\>clathon -S example2.py
    <built-in function print>
    C:\Users\Example\>_
    ```
* Clathon的config功能也可以帮助开发者在交互式环境中频繁调试类或函数，而不必重新在交互式环境中定义或导入。

## 安装教程

### 一、源码安装

#### Python源码：

1. 把源码解压到本地（或用"git clone"命令）
   `git clone git@gitee.com:MinePy/clathon.git`
2. 把安装目录添加到PATH中
3. 在用户文件夹下创建config.json
4. 安装完成

#### TAR.GZ版：

1. 把源码下载到本地
2. 使用pip安装 `pip install clathon-1.xx.x.tar.gz`
3. 把安装目录添加到PATH中
4. 在用户文件夹下创建config.json
5. 安装完成

### 二、安装包安装

1. 打开安装向导
2. 添加安装目录到PATH中
3. 在用户文件夹下创建config.json
4. 安装完成

## 使用说明

1. 运行 ` clathon`进入Clathon交互环境
2. 运行 ` clathon xxx.py`打开文件
3. 运行 ` clathon -S xxx.py`让每行代码模拟在ClathonShell中运行

## 参与贡献

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request
