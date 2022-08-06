#!/bin/bash

result=$(python test.py -v)
if [ $? -eq 0 ]
then
    echo -e "\033[0;32m Test passed, Building executable... \033[0m"
    result=$(pyinstaller --onefile main.py)
else
    echo -e "\033[0;31m Test failed, please fix code and try again. \033[0m"
fi
