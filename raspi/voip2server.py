import requests
import glob, os

def get_pcap():
    for file in glob.glob("*.pcap"):
            file_path = os.path.basename(file)
            post_pcap(file_path)
def get_networks():
    post_network("network.txt")
def post_pcap(file_path):
    url = 'http://localhost:5000/upload'

    with open(file_path, 'rb') as f:
        files = {'file': (file_path, f)}
        r = requests.post(url, files=files)

    print(r.text)

def post_network(file_path):
    url = 'http://localhost:5000/network'

    with open(file_path, 'rb') as f:
        files = {'file': (file_path, f)}
        r = requests.post(url, files=files)

    print(r.text)

def get_command():
    resp = requests.get("http://localhost:5000/getcommand")
    content = resp.content.decode("utf-8")
    return content
