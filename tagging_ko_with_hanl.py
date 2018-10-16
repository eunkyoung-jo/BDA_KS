#coding: utf-8
import os
os.environ['HANL_HOME'] = '../HANL'

import subprocess

def hanl_analyse(infn, outfn):
    cmd = '../HANL/bin/hanl < %s > %s' %(infn, outfn)
    subprocess.call(cmd, shell=True)

    outfile = open(outfn, 'r', encoding='utf-8')
    lines = outfile.readlines()
    outfile.close()
    tokens = []
    for line in lines:
        l_token = line.split(' ')
        tokens.extend(l_token)
    return tokens

all_tokens = hanl_analyse('ko_input.txt', 'ko_input.txt.out')


