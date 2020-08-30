#!/usr/bin/env bash

function info() {
    printf "\e[92;1m[INFO][$(date +%D)][$(date +%T)]$1\e[0m\n"
}

function warn() {
    printf "\e[93;1m[WARN][$(date +%D)][$(date +%T)]$1\e[0m\n"
}

function error() {
    printf "\e[91;1m[ERROR][$(date +%D)][$(date +%T)]$1\e[0m\n"
}
