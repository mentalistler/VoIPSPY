#!/bin/bash

# Create a new service file
sudo nano /etc/systemd/system/VoIPSPY.service

# Add the following content to the service file
echo "[Unit]
Description=Python script

[Service]
ExecStart=/usr/bin/python /home/kali/Desktop/VoIPSPY.py
User=root

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/VoIPSPY.service

# Reload systemd configuration
sudo systemctl daemon-reload

# Enable the service to start automatically on boot
sudo systemctl enable VoIPSPY.service

# Start the service
sudo systemctl start VoIPSPY.service
