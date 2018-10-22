#coding: utf-8
import os
os.environ['HANL_HOME'] = '../HANL'

import subprocess

def hanl_analyse(infn, outfn):
    cmd = '../HANL/bin/hanl < %s > %s' %(infn, outfn)
    subprocess.call(cmd, shell=True)
    return

hanl_analyse('ko_input.txt', 'ko_input.txt.out')


