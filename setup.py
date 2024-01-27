#coding=utf-8
"""cx-freeze打包的设置及运行脚本，非setuptools的脚本"""
from cx_Freeze import setup, Executable

#cx-freeze打包的设置和运行
setup(
    name="Clathon",
    version="1.20.1",
    description="ColorFur Application",
    author="Hardy Zhang",
    executables=[Executable("Clathon.py")]
)
