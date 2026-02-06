#!/bin/bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-full python3-pip adb fastboot nmap docker.io git curl wget tmux zram-tools
echo "dtparam=pciex1_gen=3" | sudo tee -a /boot/firmware/config.txt
curl -fsSL https://ollama.com/install.sh | sh
pip3 install dash dash-bootstrap-components psutil requests --break-system-packages
git clone https://github.com/goodtft/LCD-show.git
sudo reboot
