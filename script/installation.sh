#!/usr/bin/env bash
cd /var/lib/jenkins/workspace/sfia1pipe
sudo apt update -y

sudo apt install python3 -y

sudo apt install python3-pip -y

sudo apt install python3-venv -y

python3 -m venv venv

source ~/.bashrc

source /var/lib/jenkins/workspace/sfia1pipe/venv/bin/activate

pip3 install -r requirements.txt

cd /var/lib/jenkins/workspace/sfia1pipe/

python3 /var/lib/jenkins/workspace/sfia1pipe/app.py