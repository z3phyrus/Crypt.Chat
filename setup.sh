#!/bin/bash

export red="$(tput setaf 1)"
export blue="$(tput setaf 4)"

if [ "$(id -u)" != "0" ]; then
    echo "${red} [!] This script requires root privilege [ run with : sudo bash setup.sh] "
    exit 1
fi

echo "${blue} [!] Installing required python modules"

pip install requests
pip install sockets


echo "${blue}[!] Done ...."
