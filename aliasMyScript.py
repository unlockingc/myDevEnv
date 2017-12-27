#! /usr/bin/python3

import os
import subprocess
import sys


from pyCommon.commonOps import *

def addAlias():
    pwd = getResult("pwd")
    aliasDownload = "alias downloadMyDevEnv=\""+pwd+"/pullAndUpdate.py\""
    aliasUpload = "alias uploadMyDevEnv=\""+pwd+"/collectAndPush.py\""
    runCommand("echo \""+aliasUpload+"\">> ~/.myzshConf")
    runCommand("echo \""+aliasDownload+"\">> ~/.myzshConf")
    runCommand("echo \""+aliasDownload+"\">> ~/.bash_aliases")
    runCommand("echo \""+aliasUpload+"\">> ~/.bash_aliases")
    

if __name__ == "__main__":
    addAlias()
