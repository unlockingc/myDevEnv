#! /usr/bin/python3

import os
import subprocess
import sys


from pyCommon.commonOps import *

def addAlias():
    pwd = getResult("pwd")
    aliasDownload = "alias downloadMyDevEnv=\""+pwd+"/pullAndUpdate.py -p " + pwd + "\""
    aliasUpload = "alias uploadMyDevEnv=\""+pwd+"/collectAndPush.py -p " + pwd + "\""
    runCommand("sed -i '/^alias downloadMyDevEnv/d' ~/.myzshConf")
    runCommand("sed -i '/^alias downloadMyDevEnv/d' ~/.myzshConf")
    runCommand("echo \""+aliasUpload+"\">> ~/.myzshConf")
    runCommand("echo \""+aliasDownload+"\">> ~/.myzshConf")
    runCommand("echo \""+aliasDownload+"\">> ~/.bash_aliases")
    runCommand("echo \""+aliasUpload+"\">> ~/.bash_aliases")
    

if __name__ == "__main__":
    addAlias()
