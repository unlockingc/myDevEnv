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
    args = parser.parse_args();
    return args

def gitAction():
    print( "current working dir: " + getResult("pwd") )
    runCommand("git pull")
    

if __name__ == "__main__":
    args = parse_args()
    os.chdir(args.path)
    gitAction()
    updateConfVim()
    updateConfZsh()
    updateConfTmux()
