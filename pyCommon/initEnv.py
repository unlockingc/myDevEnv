#!/usr/bin/python2.7
import os
import commands
import platform
from softwareDict import *
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
    status, output = commands.getstatusoutput(commandString)
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


if __name__ == '__main__':    
    dist = platform.dist()
    distName = dist[0]
    print("get distibution information as:" + str(dist) + "\n==================")
    if distName.lower() == "ubuntu":
        installSoftware("build-essential git")
    else:
        runCommand("sudo yum groupinstall \"Development Tools\"")
        runCommand("sudo yum install epel-release.noarch -y")
    installSoftware("git openssl-dev bzip2-dev expat-dev gdbm-dev readline-dev sqlite-dev")
    runCommand("[ ! -d ~/.pyenv ] && git clone https://github.com/pyenv/pyenv.git ~/.pyenv || true")
    runCommand("echo \'export PYENV_ROOT=\"$HOME/.pyenv\"\' | sudo tee /etc/profile.d/mypyenv.sh")
    runCommand("echo \'export PYTHON_CONFIGURE_OPTS=\"--enable-shared\"\' | sudo tee -a /etc/profile.d/mypyenv.sh")
    runCommand("echo \'export PATH=\"$PYENV_ROOT/bin:$PATH\"\' | sudo tee -a /etc/profile.d/mypyenv.sh")
    runCommand("echo -e \'if command -v pyenv 1>/dev/null 2>&1; then\\n  eval \"$(pyenv init -)\"\\nfi\'  | sudo tee -a /etc/profile.d/mypyenv.sh")
    runCommand("source /etc/profile")
    pythonVersions = getResult("pyenv versions")
    if pythonVersions.find("3.6.4") == -1:
        runCommand("pyenv install 3.6.4")
    else:
        print("3.6.4 already installed!!!")
    runCommand("pyenv global 3.6.4")
   

