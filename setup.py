#coding=utf-8
from cx_Freeze import setup, Executable
setup(
    name="Clathon",
    version="1.20.1",
    description="ColorFur Application",
    author="Hardy Zhang",
    executables=[Executable("Clathon.py")]
)
