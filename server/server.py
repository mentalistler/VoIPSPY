from flask import Flask, request

app = Flask(__name__)

command= None


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file.filename.endswith('.pcap'):
        file.save('received_file.pcap')
        return 'File uploaded'
    else:
        return 'Invalid file format'
@app.route('/network', methods=['POST'])
def upload_network():
    file = request.files['file']
    if file.filename.endswith('.txt'):
        file.save('network.txt')
        return 'File uploaded'
    else:
        return 'Invalid file format'

@app.route('/command', methods=['GET'])
def set_command():
    global command
    _command = request.args.get('command')
    command = _command
    return f'Command Success, {command}!'
@app.route('/getcommand')
def get_command():
    global command
    return str(command)

if __name__ == '__main__':
    app.run()
