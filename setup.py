import sys
import os
from cx_Freeze import setup, Executable
#Add your file ico
files= ['logo.ico']

target = Executable(
    script="Update.py",
    base="Win32GUI",
    icon="logo.ico"
)

setup(
    name = "Update",
    version = "1.0",
    description = "Update Mu",
    author = "Ermes",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
)    