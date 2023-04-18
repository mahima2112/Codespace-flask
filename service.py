# pylint: skip-file
import os
import sys

service_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
sys.path.append(service_path)
from app import server

if __name__ == "__main__":
    
    server.run(debug=True, port=5100)
