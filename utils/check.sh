#!/bin/bash

echo -e "\n\033[1;36mRunning $1check...\033[0m"
find -name "*.md" | xargs python3 -B utils/$1check.py
