#! /usr/bin/python3

import os
import subprocess
import sys
from tmux.install_tmux import *
from vim.install_SpaceVim import *
from zsh.install_zsh import *


from pyCommon.commonOps import *

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
    runCommand("git add --all")
    runCommand("git commit -m \""+ getVersion()  +"\"")
    runCommand("git push")
    

if __name__ == "__main__":
    collectTmux()
    collectVim()
    collectZsh()
    gitAction()
