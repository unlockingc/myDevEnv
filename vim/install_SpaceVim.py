#! /usr/bin/env python

import os
import subprocess
import sys
sys.path.append("..")

from pyCommon.commonOps import *


def upgradeVim():
    uninstallSoftware("vim")
    if distName.lower() == "ubuntu":
        runCommand("sudo apt-get install -y --force-yes libncurses5-dev libgnome2-dev libgnomeui-dev \
            libgtk2.0-dev libatk1.0-dev libbonoboui2-dev \
            libcairo2-dev libx11-dev libxpm-dev libxt-dev python-dev \
            python3-dev ruby-dev lua5.1 liblua5.1-dev libperl-dev git")
    else:
        runCommand("sudo yum install -y ruby ruby-devel lua lua-devel luajit \
            luajit-devel ctags git python python-devel \
            python3 python3-devel tcl-devel \
            perl perl-devel perl-ExtUtils-ParseXS \
            perl-ExtUtils-XSpp perl-ExtUtils-CBuilder \
            perl-ExtUtils-Embed")

    aptRequire= ["cmake python-dev python env python-pip ncurses-dev cscope"]
    submoduleName = "VimSource"
    def buildFunction():
        runCommand("make distclean")
        runCommand("./configure --with-features=huge \
            --enable-multibyte \
            --enable-rubyinterp=yes \
            --enable-pythoninterp=yes \
            --enable-python3interp=yes \
            --enable-perlinterp=yes \
            --enable-luainterp=yes \
            --enable-gui=gtk2 \
            --enable-cscope \
            --prefix=/usr/local")
        runCommand("make")
        runCommand("sudo make install")

    installFromSubmodule("vim8.0", submoduleName, aptRequire,buildFunction,"vim")  

def installNeoVim():
    installSoftware("neovim")

def installSpaceVim():
    installSoftware("curl")
    runCommand("curl -sLf https://spacevim.org/install.sh | bash")

def installYCM():
    installSoftware("ctags env python env python-dev python-pip")
    currentDir = getResult("pwd")
    runCommand("[ ! -d ~/.cache/vimfiles/repos/github.com/Valloric/ ] && mkdir ~/.cache/vimfiles/repos/github.com/Valloric || true")
    os.chdir(os.path.expanduser("~/.cache/vimfiles/repos/github.com/Valloric"))
    runCommand("[ ! -d YouCompleteMe ] && git clone https://github.com/Valloric/YouCompleteMe.git || true")
    os.chdir("YouCompleteMe")
    runCommand("export PYTHON_CONFIGURE_OPTS=\"--enable-shared\"")
    runCommand("git submodule update --init --recursive")
    runCommand("./install.py --clang-completer --go-completer")
    runCommand("cp third_party/ycmd/examples/.ycm_extra_conf.py ~/.vim/")
    os.chdir(currentDir)


def copyMyConf():
    runCommand("[ ! -d ~/.SpaceVim.d ] && mkdir ~/.SpaceVim.d || true")
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

def installVim():
    installSoftware("vim")
    vimVersion = getResult("vim --version | grep \"VIM - Vi IMprove\" | awk '{print $5}'")

    if float(vimVersion) < 8.0 :
        print("vim version: " + vimVersion + " ++++ need upgrade!")
        upgradeVim()
    else:
        print("vim version: " + vimVersion + " ===do not need upgrade!")


def installVimAll():
    os.chdir("vim")
    installVim()
    #installNeoVim()
    installSpaceVim()
    copyMyConf()
    installYCM()
    os.chdir("../")

def installVimAllTest():
    print("installVim")
    
    
if __name__ == "__main__":
   os.chdir("../")
   installVimAll()
