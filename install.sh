#!/bin/bash

# Check if the script is running on Raspbian
if ! grep -q "Raspbian" /etc/os-release; then
    echo "This script is designed to run on Raspbian."
    exit 1
fi

# Check if the script is running as root
if [ "$EUID" -ne 0 ]; then
    echo "This script needs superuser privileges. You will be prompted for sudo password."
    sudo "$0" "$@"
    exit
fi

echo "Installing necessary dependencies for PiNtuitive..."

# Update system and install wmctrl and python3-tk
sudo apt-get update
sudo apt-get install -y wmctrl python3-tk
sudo apt-get install -y x11-utils
sudo apt-get install -y matchbox-keyboard
sudo apt-get install -y at-spi2-core
