#! /usr/bin/python3

import os
import subprocess
import sys
sys.path.append("..")

from pyCommon.commonOps import *


def upgradeVim():
    runCommand("sudo apt-get remove -y vim")
    aptRequire= ["cmake build-essential python3-dev python3 python3-pip ncurses-dev"]
    submoduleName = "VimSource"
    def buildFunction():
        runCommand("make")
        runCommand("sudo make install")

    installFromSubmodule("vim8.0", submoduleName, aptRequire,buildFunction)


def installNeoVim():
    installSoftWare("neovim")

def installSpaceVim():
    installSoftWare("curl")
    runCommand("curl -sLf https://spacevim.org/install.sh | bash")

def installYCM():
    installSoftWare("ctags python3 python3-dev python3-pip")
    currentDir = getResult("pwd")
    runCommand("[ ! -d ~/.cache/vimfiles/repos/github.com/Valloric/ ] && mkdir ~/.cache/vimfiles/repos/github.com/Valloric || true")
    os.chdir(os.path.expanduser("~/.cache/vimfiles/repos/github.com/Valloric"))
    runCommand("[ ! -d YouCompleteMe ] && git clone https://github.com/Valloric/YouCompleteMe.git || true")
    os.chdir("YouCompleteMe")
    runCommand("git submodule update --init --recursive")
    runCommand("./install.py --clang-completer --go-completer")
    runCommand("cp third_party/ycmd/examples/.ycm_extra_conf.py ~/.vim/")
    os.chdir(currentDir)


def copyMyConf():
    runCommand("[ -f ~/.SpaceVim.d/init.vim ] && mv ~/.SpaceVim.d/init.vim ~/.SpaceVim.d/init.vim.backup.myDevEnv || true")
    runCommand("cp ./init.vim ~/.SpaceVim.d/init.vim")
    
    runCommand("[ -f ~/.vim/autoload/SpaceVim/layers/lang/go.vim ] && mv ~/.vim/autoload/SpaceVim/layers/lang/go.vim ~/.vim/autoload/SpaceVim/layers/lang/go.vim.backup.myDevEnv || true")
    runCommand("cp ./go.vim ~/.vim/autoload/SpaceVim/layers/lang/go.vim")


def updateConfVim():
    os.chdir("vim")
    runCommand("[ -f ~/.SpaceVim.d/init.vim ] && mv -f ~/.SpaceVim.d/init.vim ~/.SpaceVim.d/init.vim.backup.myDevEnv || true")
    runCommand("cp ./init.vim ~/.SpaceVim.d/init.vim")
    
    runCommand("[ -f ~/.vim/autoload/SpaceVim/layers/lang/go.vim ] && mv -f ~/.vim/autoload/SpaceVim/layers/lang/go.vim ~/.vim/autoload/SpaceVim/layers/lang/go.vim.backup.myDevEnv || true")
    runCommand("cp ./go.vim ~/.vim/autoload/SpaceVim/layers/lang/go.vim")
    os.chdir("../")

def collectVim():
    os.chdir("vim")
    runCommand("[ -f init.vim ] && rm init.vim || true")
    runCommand("[ -f ~/.SpaceVim.d/init.vim ] && cp ~/.SpaceVim.d/init.vim init.vim")
    runCommand("[ -f go.vim ] && rm go.vim || true")
    runCommand("[ -f ~/.vim/autoload/SpaceVim/layers/lang/go.vim ] && cp ~/.vim/autoload/SpaceVim/layers/lang/go.vim go.vim")
    os.chdir("../")

def installVimAll():
    os.chdir("vim")
    upgradeVim()
    installNeoVim()
    installSpaceVim()
    copyMyConf()
    installYCM()
    os.chdir("../")

def installVimAllTest():
    print("installVim")
    
    
if __name__ == "__main__":
   os.chdir("../")
   installVimAll()
