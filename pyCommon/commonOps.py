#!/usr/bin/python3
import subprocess
import platform
import os


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

def installSoftWare(softwareName):
    """TODO: Docstring for installSoftWare.

    :softwareName: as softwareName
    :returns: success: True or False

    """
    command = "install -y " + softwareName
    if distName.lower()=="ubuntu":
        command = "sudo apt-get " + command
    elif distName.lower()=="centos" or distName.lower()=="redhat":
        command = "sudo yum " + command
    elif distName.lower()=="macos":
        #command = "sudo brew install " + command
        print("Error, Mac Os has not been covered!!!")
    retCode = subprocess.call(command.split())
    if retCode==0:
        return True
    else:
        print("Failed Due to Command error: " + command)
        exit(1)

def installFromSource(name,git,aptRequire, buildCommands):
    for softwareName in aptRequire:
        installSoftWare(softwareName)
    tempDir = name + ".build"
    runCommand("[ -d "+tempDir +" ] && rm " + tempDir + " -rf || true")
    runCommand("mkdir " + tempDir)
    os.chdir(tempDir)
    runCommand("git clone " + git + " ./" + name)
    os.chdir(name)
    buildCommands()
    os.chdir("../../")
    runCommand("[ -d "+tempDir +" ] && rm " + tempDir + " -rf || true")

    
backupNumber = 2
dist = platform.dist()
distName = dist[0]
print("get distibution information as:" + str(dist) + "\n==================")


