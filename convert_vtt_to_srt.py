#! /usr/bin/env python3
import sys
import re
import os
def copy(src, dst):
    with open(src, 'rb') as sr:
        data = sr.read()
        with open(dst, 'wb') as dr:
            dr.write(data)
def replace(fc):
    return re.sub('\.',',',fc)
def remove_WEBVTT(fc):
    return re.sub('WEBVTT','',fc)
def main():
    input_list = sys.argv
    pyname, src_addr = input_list[0], input_list[1]
    dirs = os.listdir(src_addr)
    os.chdir(src_addr)
    for fl in dirs:
        fn, ext = os.path.splitext(fl)
        if ext.lstrip('.') == 'vtt':
            srt_file = fl.replace('vtt','srt')
            copy(fl, srt_file)
            with open(srt_file,'r') as dstr:
                file_content = dstr.read()
                file_content = replace(file_content)
                file_content = remove_WEBVTT(file_content)
            with open(srt_file,'w') as dstw:
                dstw.write(file_content)
        else:
            continue
    print('Subtitles Converted Successfully :)')
if __name__ == "__main__":
    main()
