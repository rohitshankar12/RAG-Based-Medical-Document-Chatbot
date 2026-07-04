import subprocess
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

server = subprocess.Popen(
    ["uvicorn", "main:app", "--reload"],
    cwd=os.path.join(BASE_DIR, "server")
)

time.sleep(3)  # Wait for backend to start

client = subprocess.Popen(
    ["streamlit", "run", "app.py"],
    cwd=os.path.join(BASE_DIR, "client")
)

client.wait()
server.terminate()