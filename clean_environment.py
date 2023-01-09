import requests

def clean_environment():
    requests.get('http://127.0.0.1:5000/stop_server')
    requests.get('http://127.0.0.1:5001/stop_server')

if __name__ == '__main__':
    clean_environment()