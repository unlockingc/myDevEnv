#!/usr/bin/env python
import json
import os


projectDirTemp = os.getcwd()
projectDirTemp = projectDirTemp[0:projectDirTemp.find("myDevEnv")+len("myDevEnv")]
jsonFile = open(projectDirTemp + "/pyCommon/conf.json")
jsonConfString = jsonFile.read()
jsonFile.close()


jsonConfDict = json.loads(jsonConfString)
softwareVersion = jsonConfDict["softwareVersion"]
downloadLink = jsonConfDict["downloadLink"]
downloadFileName = jsonConfDict["downloadFileName"]

ubuntuDict = {\
"automake" : "automake",\
"pkg-config" : "pkg-config",\
"m4" : "m4",\
"libtool" : "libtool",\
"libevent-dev" : "libevent-dev",\
"ncurses-dev" : "ncurses-dev",\
"env" : "",\
"ncurses-dev" : "ncurses-dev",\
"python" : "python",\
"python-pip" : "python-pip",\
"python-dev" : "python-dev",\
"cscope" : "cscope",\
"git":"git",\
"cmake":"cmake", \
"xclip":"xclip", \
"tmux":"tmux", \
"neovim":"neovim", \
"curl":"curl", \
"ctags":"ctags", \
"vim":"vim", \
"zsh":"zsh", \
"curl":"curl", \
"wget":"wget", \
"openssl-dev" : "openssl-dev", \
"bzip2-dev" : "bzip2-dev", \
"expat-dev" : "expat-dev", \
"gdbm-dev" : "gdbm-dev", \
"readline-dev" : "readline-dev", \
"sqlite-dev" : "sqlite-dev", \
}

centosDict = {\
"automake" : "automake",\
"pkg-config" : "pkgconfig",\
"m4" : "m4",\
"libtool" : "libtool",\
"libevent-dev" : "libevent-devel",\
"ncurses-dev" : "ncurses-devel",\
"env" : "env",\
"ncurses-dev" : "ncurses-devel",\
"python" : "python",\
"python-pip" : "python-pip",\
"python-dev" : "python-devel",\
"cscope" : "cscope",\
"git":"git",\
"cmake":"cmake", \
"xclip":"xclip", \
"tmux":"tmux", \
"neovim":"neovim", \
"curl":"curl", \
"ctags":"ctags", \
"vim":"vim", \
"zsh":"zsh", \
"curl":"curl", \
"wget":"wget", \
"openssl-dev" : "openssl-devel", \
"bzip2-dev" : "bzip2-devel", \
"expat-dev" : "expat-devel", \
"gdbm-dev" : "gdbm-devel", \
"readline-dev" : "readline-devel", \
"sqlite-dev" : "sqlite-devel", \
}

softwareDictionary = { "ubuntu" : ubuntuDict, "centos" : centosDict }

if __name__ == '__main__':
    print(softwareDictionary['ubuntu']['cmake'])
