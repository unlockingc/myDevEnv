#! /usr/bin/python3

import os
import subprocess
import sys
sys.path.append("..")

from pyCommon.commonOps import *

def installZsh():
    installSoftWare("zsh")

def installOhMyZsh():
    installSoftWare("curl wget")
    runCommand("sh -c \"$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)\"")
    #runCommand("chsh -s /bin/bash")   

def installPlugins():
    #auto-suggestion
    runCommand("[ ! -d ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions ] && git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions || true")

def copyMyConf():
    runCommand("[ -f ~/.zshrc ] && mv ~/.zshrc ~/.zshrc.backup.myDevEnv || true")
    runCommand("cp .zshrc ~/.zshrc")
    
    
def installZshAll():
    os.chdir("zsh")
    installZsh()
    installOhMyZsh()
    installPlugins()
    copyMyConf()
    os.chdir("../")

def installZshAllTest():
    print("installZsh")
    
