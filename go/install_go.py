#! /usr/bin/env python
import time
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
    successDir = {}
    command = "go get -u "
    for key in tools:
        result = getResult('command -v '+key+' && echo 1 || echo 0')
        if result == '0':
            tempCommand = command + tools[key]
            print('download: ' + key + " \n\t\t" + command )
            ret = runCommandFaultTolerant(tempCommand)
            if ret:
                successDir[key] = 1
            else:
                successDir[key] = 0
        else:
            print('already have: ' + key)
            successDir[key] = 2
    print("\033[1;37;46mGo get Finished, installed pkg are:  \033[0m")
    for key in successDir:
        if successDir[key] == 1:
            print("\033[30;1m"+ key +"[New]  \033[0m")
        else:
            if successDir[key] == 2:
                print("\033[36;1m"+key+"[Already] \033[0m")
            else:
                print("\033[31;1m"+ key +"[Failed]  \033[0m")
    time.sleep(2)


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
