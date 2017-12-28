#! /usr/bin/python3

import os
import subprocess
import sys
sys.path.append("..")


from pyCommon.commonOps import *

def InstallTmux():
    installSoftWare("xclip")
    runCommand("[ -d ~/.tmux/plugins/tpm ] && rm -rf ~/.tmux/plugins/tpm || true")
    command = "git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm"
    runCommand(command)

def InstallTpm():
    installSoftWare("tmux")

def copyConf():
    runCommand("[ -f ~/.tmux.conf ] && mv ~/.tmux.conf ~/.tmux.conf.backup.myDevEnv || true")
    runCommand("cp .tmux.conf ~/.tmux.conf")
    

def updateConfTmux():
    os.chdir("tmux")
    runCommand("[ -f ~/.tmux.conf ] && mv -f ~/.tmux.conf ~/.tmux.conf.backup.myDevEnv || true")
    runCommand("cp .tmux.conf ~/.tmux.conf")
    os.chdir("../")    

def upgradeTmux():
    aptRequire= ["automake","pkg-config","m4","libtool","libevent-dev","ncurses-dev"]
    gitUrl = "https://github.com/tmux/tmux.git"
    def buildFunction():
        runCommand("sh autogen.sh")
        runCommand("./configure && make")
        runCommand("sudo make install")

    installFromSource("tmux",gitUrl,aptRequire,buildFunction)

def collectTmux():
    os.chdir("tmux")
    runCommand("[ -f .tmux.conf ] && rm .tmux.conf || true")
    runCommand("[ -f ~/.tmux.conf ] && cp ~/.tmux.conf .tmux.conf")
    os.chdir("../")

def installTmuxAll():
    os.chdir("tmux")
    InstallTmux()
    InstallTpm()
    copyConf()
    temp = getResult("tmux -V")
    version = temp.split()[1]
    print( "current tmux version:" + version )
    if version.lower() != "master":
        if float( version ) < 2.2:
            runCommand("sudo apt-get remove tmux -y")
            upgradeTmux()
    os.chdir("../")

def installTmuxAllTest():
    print("installTmuxAllmux")

if __name__ == "__main__":
   os.chdir("../")
   installTmuxAll()
