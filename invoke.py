#!.venv/bin/python3

import requests
import json

from pathlib import Path

home_data = json.loads(Path("data", "home.json").read_text())
square_data = json.loads(Path("data", "square.json").read_text())

ENDPOINT = "http://localhost:8000/2015-03-31/functions/function/invocations"

home_response = requests.get(ENDPOINT, json=home_data).json()
square_response = requests.get(ENDPOINT, json=square_data).json()

print("Home response:")
print(json.dumps(home_response, indent=4))

print("Sqare response:")
print(json.dumps(square_response, indent=4))
