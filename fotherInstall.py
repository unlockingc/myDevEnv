#! /usr/bin/env python

import os
import subprocess
import sys
from tmux.install_tmux import *
from vim.install_SpaceVim import *
from zsh.install_zsh import *
from aliasMyScript import *


from pyCommon.commonOps import *

if __name__ == "__main__":
    installTmuxAll()
    installZshAll()
    installVimAll()
    addAlias()
