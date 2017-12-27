#! /usr/bin/python3

import os
import subprocess
import sys
from tmux.install_tmux import *
from vim.install_SpaceVim import *
from zsh.install_zsh import *


from pyCommon.commonOps import *

def gitAction():
    runCommand("git pull")
    

if __name__ == "__main__":
    gitAction()
    updateConfVim()
    updateConfZsh()
    updateConfTmux()
