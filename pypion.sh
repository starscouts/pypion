#!/bin/bash

cmd=python

if ! command -v python &> /dev/null
then
    if ! command -v python &> /dev/null
    then
        cmd=python3.10
    else
        cmd=python3
    fi
else
    cmd=python
fi

PYGAME_HIDE_SUPPORT_PROMPT=hide $cmd main.py