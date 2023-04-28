#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
src_root_path = os.path.realpath(os.path.dirname(__file__) + '/../')
sys.path.append(src_root_path)
proto_path = os.path.realpath(src_root_path + '/proto/')
sys.path.append(proto_path)

from PyInstaller.__main__ import run
# -F:打包成一个EXE文件
# -w:不带console输出控制台，window窗体格式
# --paths：依赖包路径
# --icon：图标
# --noupx：不用upx压缩
# --clean：清理掉临时文件
#'--icon', '../icons/brainco.png',
# '--hidden-import=queue',
# '--icon', 'D:\\GitHub\\hardware-dev-tools\\wifi_configure\\icons\\brain.ico',

if __name__ == '__main__':
    opts = ['--paths=D:\\ProgramData\\Miniconda3\\envs\\crimson-env\\Lib\\site-packages\\PyQt5\\Qt\\bin',
            '--paths=D:\\ProgramData\\Miniconda3\\envs\\crimson-env\\Lib\\site-packages\\PyQt5\\Qt\\plugins',
            '--add-data=D:\\BrainCo\\GitHub\\crimson-sdk\\python\\libcmsn;libcmsn',
            '--noupx', '--clean', '--name', u'Crimson_Sdk_Tool_20210112',
            '.\\gui.py']
    run(opts)