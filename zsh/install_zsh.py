#! /usr/bin/env python

import os
import subprocess
import sys
sys.path.append("..")

from pyCommon.commonOps import *

def installZsh():
    installSoftware("zsh")

def installOhMyZsh():
    installSoftware("curl wget")
    homePath = os.path.expanduser("~")
    newHomepath = homePath.replace("/","\/" )
    #sed -n 's/\/home\/.*\/\.oh/${HOME}/p' ~/.zshrc
    runCommand("[ -f ~/.zshrc ] && sed -i 's/\/home\/.*\/.oh/"+newHomepath+"\/.oh/g' ~/.zshrc || true")
    runCommand("[ ! -f install.sh ] && wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O install.sh || true")
    runCommand("chmod u+x install.sh")
    runCommand("sed -i \"/env zsh/d\" install.sh")
    runCommand("./install.sh")
    #runCommand("chsh -s /bin/bash")   

def installPlugins():
    #auto-suggestion
    runCommand("[ ! -d ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions ] && git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions || true")

def copyMyConf():
    runCommand("[ -f ~/.zshrc ] && mv ~/.zshrc ~/.zshrc.backup.myDevEnv || true")
    runCommand("cp .zshrc ~/.zshrc")
    homePath = os.path.expanduser("~")
    newHomepath = homePath.replace("/","\/" )
    runCommand("sed -i 's/\/home\/.*\/.oh/"+newHomepath+"\/.oh/g' ~/.zshrc")

def updateConfZsh():
    os.chdir("zsh")
    runCommand("[ -f ~/.zshrc ] && mv -f ~/.zshrc ~/.zshrc.backup.myDevEnv || true")
    runCommand("cp .zshrc ~/.zshrc")
    runCommand("[ -f ~/.zshrc ] && sed -i 's/\/home\/.*\/.oh/"+newHomepath+"\/.oh/g' ~/.zshrc || true")
    os.chdir("../")

def collectZsh():
    os.chdir("zsh")
    runCommand("[ -f .zshrc ] && rm .zshrc || true")
    runCommand("[ -f ~/.zshrc ] && cp ~/.zshrc .zshrc")
    os.chdir("../")
    
def installZshAll():
    os.chdir("zsh")
    installZsh()
    installOhMyZsh()
    installPlugins()
    copyMyConf()
    os.chdir("../")

def installZshAllTest():
    print("installZsh")

if __name__ == "__main__":
   os.chdir("../")
   installZshAll()
