#!/usr/bin/env bash

#initalize
base_dir=$(realpath $BASH_SOURCE)
base_dir=$(dirname $base_dir)

source $base_dir/shell/utils.sh

# check python version and pyenv, if not, install it
which pyenv >/dev/null
if [[ $? != 0 ]]; then
    error "pyenv not installed"
else
    info "pyenv installed"
fi
