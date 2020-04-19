#! /usr/bin/env python3
"""
-*- coding: utf-8 -*-
v1.0
copyright (c) 2020 Omid Akhgary. all rights reserved.
licence: GPL3
email: omid7798@gmail.com
"""

import sys
import re
import os
class Color():
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    NOCOLOR = '\033[m'

    @staticmethod
    def colorfull(**kwargs):
        text   = kwargs.get("text", "")
        color  = kwargs.get("color", Color.NOCOLOR)

        return str(color + text)
class Convert():
    def __init__(self, **kwargs):
        self.path       = kwargs.get("path", None)
        self.real_name, self.extension  = os.path.splitext(self.path)

    def is_vtt(self):
        if self.extension.lstrip('.') == 'vtt':
            return True
        else:
            return False

    def copy(self, src, dst):
        with open(src, 'rb') as sr:
            data = sr.read()
            with open(dst, 'wb') as dr:
                dr.write(data)
    def replace_(self, fc):
        return re.sub('\.',',',fc)
    def remove_WEBVTT(self, fc):
        return re.sub('WEBVTT','',fc)
    def convert_(self):
        srt_file = self.path.replace('vtt','srt')
        self.copy(self.path, srt_file)
        with open(srt_file,'r') as dstr:
            file_content = dstr.read()
            file_content = self.replace_(file_content)
            file_content = self.remove_WEBVTT(file_content)
        with open(srt_file,'w') as dstw:
            dstw.write(file_content)

def main():
    print("converting...")
    count_performs = 0
    try:
        src_addr = os.path.abspath(os.path.join(sys.argv[1]))
    except:
        print(Color.colorfull(color=Color.RED,text='Unknown argument'))
        sys.exit(1)

    if os.path.exists(src_addr):
        if os.path.isdir(src_addr):
            dirs = os.listdir(src_addr)
            os.chdir(src_addr)
            for files in dirs:
                convert_vtt = Convert(path=files)
                if convert_vtt.is_vtt():
                    convert_vtt.convert_()
                    count_performs += 1
                    print(Color.colorfull(color=Color.NOCOLOR, text='%s --> %s.srt' % (files, convert_vtt.real_name)), Color.colorfull(color=Color.GREEN, text='done'))
                else:
                    continue
        elif os.path.isfile(src_addr):
            convert_vtt = Convert(path=src_addr)
            if convert_vtt.is_vtt():
                convert_vtt.convert_()
                count_performs += 1
                print(Color.colorfull(color=Color.NOCOLOR, text='%s --> %s.srt' % (src_addr, convert_vtt.real_name)), Color.colorfull(color=Color.GREEN, text='done'))

        if count_performs > 0:
            print(Color.colorfull(color=Color.GREEN, text='%i Subtitles Converted Successfully.' % count_performs))
        else:
            print(Color.colorfull(color=Color.YELLOW, text='There are no vtt subtitle to convert.'))
    else:
        print(Color.colorfull(color=Color.RED, text='path %s does not exists.' % src_addr))
if __name__ == "__main__":
    main()