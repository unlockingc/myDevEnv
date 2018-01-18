#!/usr/bin/env python
import os
import subprocess
import platform


command = "git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins1"
print(command.split())
print("===================")
retCode = subprocess.call(command.split())
