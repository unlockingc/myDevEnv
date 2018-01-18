#!/usr/bin/env python
import subprocess
import platform
import os
import sys

sys.path.append("..")
from pyCommon.softwareDict import *

def runCommand(commandString):
    """TODO: Docstring for runCommand.
    :returns: success: True or False

    """
    #retCode = subprocess.call(commandString.split())
    retCode = os.system(commandString)
    if retCode==0:
        return True
    else:
        print("Failed Due to Command error: " + commandString)
        exit(1)

def getResult(commandString):
    status, output = subprocess.getstatusoutput(commandString)
    if status==0:
        return output
    else:
        print("Failed Due to Command error: " + commandString)


def getSoftwareNameOnDist(softwareName):
    templist = softwareName.split()
    result = ""
    for temp in templist:
        result = result + " " + softwareDictionary[distName.lower()][temp]
    return result
 
def uninstallSoftware(softwareName):
    softwareName = getSoftwareNameOnDist(softwareName)
    command = "remove -y " + softwareName
    if distName.lower()=="ubuntu":
        command = "sudo apt-get " + command + " --force-yes"
    elif distName.lower()=="centos" or distName.lower()=="redhat":
        command = "sudo yum " + command
    elif distName.lower()=="macos":
        #command = "sudo brew install " + command
        print("Error, Mac Os has not been covered!!!")
    else:
        print("Error, OS not supported: " + distName)
    retCode = os.system(command)
    if retCode==0:
        return True
    else:
        print("Failed Due to Command error: " + command)
        exit(1)



def installSoftware(softwareName):
    """TODO: Docstring for installSoftWare.

    :softwareName: as softwareName
    :returns: success: True or False

    """
    softwareName = getSoftwareNameOnDist(softwareName)
    command = "install -y  " + softwareName
    if distName.lower()=="ubuntu":
        command = "sudo apt-get " + command + " --force-yes"
    elif distName.lower()=="centos" or distName.lower()=="redhat":
        command = "sudo yum " + command
    elif distName.lower()=="macos":
        #command = "sudo brew install " + command
        print("Error, Mac Os has not been covered!!!")
    else:
        print("Error, OS not supported: " + distName)
    retCode = os.system(command)
    if retCode==0:
        return True
    else:
        print("Failed Due to Command error: " + command)
        exit(1)



def installFromSubmodule(name,submoduleName,aptRequire, buildCommands, subFolder):
    for softwareName in aptRequire:
        installSoftware(softwareName)
    pwd=getResult("pwd")
    
    os.chdir(projectDir)
    runCommand("git submodule update --init ./" + subFolder + "/" + submoduleName)
    os.chdir(pwd)
    
    os.chdir(submoduleName)
    buildCommands()
    os.chdir("../")

    
projectDir = getResult("pwd")
projectDir = projectDir[0:projectDir.find("myDevEnv")+len("myDevEnv")]
backupNumber = 2
dist = platform.dist()
distName = dist[0]
print("get distibution information as:" + str(dist) + "\n==================")


