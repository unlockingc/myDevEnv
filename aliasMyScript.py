#! /usr/bin/env python

import os
import subprocess
import sys


from pyCommon.commonOps import *

def addAlias():
    pwd = getResult("pwd")
    aliasDownload = "alias downloadMyDevEnv=\\\""+pwd+"/pullAndUpdate.py -p " + pwd + "\\\""
    aliasUpload = "alias uploadMyDevEnv=\\\""+pwd+"/collectAndPush.py -p " + pwd + "\\\""
    runCommand("[ -f ~/.myzshConf ] && sed -i '/^alias downloadMyDevEnv/d' ~/.myzshConf || true")
    runCommand("[ -f ~/.myzshConf ] && sed -i '/^alias uploadMyDevEnv/d' ~/.myzshConf || true")
    runCommand("[ -f ~/.bash_aliases ] && sed -i '/^alias downloadMyDevEnv/d' ~/.bash_aliases || true")
    runCommand("[ -f ~/.bash_aliases ] && sed -i '/^alias uploadMyDevEnv/d' ~/.bash_aliases || true")
    
    runCommand("echo \""+aliasUpload+"\">> ~/.myzshConf")
    runCommand("echo \""+aliasDownload+"\">> ~/.myzshConf")
    runCommand("echo \""+aliasDownload+"\">> ~/.bash_aliases")
    runCommand("echo \""+aliasUpload+"\">> ~/.bash_aliases")
    

if __name__ == "__main__":
    addAlias()
