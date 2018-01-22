#! /usr/bin/env python

import os
import subprocess
import sys
sys.path.append("..")


from pyCommon.commonOps import *

def InstallGo():
    downloadSoftware("go")
    command = "sudo tar -C /usr/local -xzf go1.9.2.linux-amd64.tar.gz"
    runCommand(command)
    command = "echo \'export PATH=$PATH:/usr/local/go/bin\' | sudo tee /etc/profile.d/mygoenv.sh"
    runCommand(command)
    me = getResult("whoami")
    myGoPath = ""
    if me == "houyx":
        myGoPath = "~/development/go"
    else:
        myGoPath = "~/houyx/development/go"
    runCommand("mkdir -p " +  myGoPath)

    command = "echo \'export GOPATH="+ myGoPath +"\' | sudo tee -a /etc/profile.d/mygoenv.sh"
    runCommand(command)

    runCommand("source /etc/profile")



    command = "echo \'export PATH=$PATH:$(go env GOPATH)/bin\' | sudo tee -a /etc/profile.d/mygoenv.sh"
    runCommand(command)
    runCommand("source /etc/profile")




def InstallGoTools():
    tools = {\
       'asmfmt':        'github.com/klauspost/asmfmt/cmd/asmfmt',\
       'errcheck':      'github.com/kisielk/errcheck',\
       'fillstruct':    'github.com/davidrjenni/reftools/cmd/fillstruct',\
       'gocode':        'github.com/nsf/gocode',\
       'godef':         'github.com/rogpeppe/godef',\
       'gogetdoc':      'github.com/zmb3/gogetdoc',\
       'goimports':     'golang.org/x/tools/cmd/goimports',\
       'golint':        'github.com/golang/lint/golint',\
       'gometalinter':  'github.com/alecthomas/gometalinter',\
       'gomodifytags':  'github.com/fatih/gomodifytags',\
       'gorename':      'golang.org/x/tools/cmd/gorename',\
       'gotags':        'github.com/jstemmer/gotags',\
       'guru':          'golang.org/x/tools/cmd/guru',\
       'impl':          'github.com/josharian/impl',\
       'keyify':        'github.com/dominikh/go-tools/cmd/keyify',\
       'motion':        'github.com/fatih/motion',\
     }

    command = "go get -u "
    for key in tools:
        result = getResult('command -v '+key+' && echo 1 || echo 0')
        if result == '0':
            tempCommand = command + tools[key]
            print('download: ' + key)
            runCommand(tempCommand)
        else:
            print('already have: ' + key)

def installGoAll():
    os.chdir("go")
    InstallGo()
    InstallGoTools()
    os.chdir("../")

def installGoAllTest():
    print("installTmuxAllmux")

if __name__ == "__main__":
   os.chdir("../")
   installGoAll()
