#! /usr/bin/python3

import os
import subprocess
import sys
from tmux.install_tmux import *
from vim.install_SpaceVim import *
from zsh.install_zsh import *


from pyCommon.commonOps import *

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description = "path is the only arg!!")
    help = "path to exce the cammand, default: myDevEnv git"
    parser.add_argument( '-p','--path', help=help, default=getResult("pwd"))

def getVersion():
    versionNumber = 0
    versionFile = open("version.log","a+")
    versionFile.seek(0)
    versionString = versionFile.read()
    print(versionString)
    print("======================")
    if versionString != "" :
        versionNumber = int(versionString)

    versionFile.seek(0)
    versionFile.truncate()
    versionFile.write(str(versionNumber + 1))
    return str(versionNumber)
    

def gitAction():
    runCommand("git submodule update")
    runCommand("git add --all")
    runCommand("git commit -m \""+ getVersion()  +"\"")
    runCommand("git push")
    

if __name__ == "__main__":
    args = parse_args()
    os.chdir(args.path)
    collectTmux()
    collectVim()
    collectZsh()
    gitAction()
