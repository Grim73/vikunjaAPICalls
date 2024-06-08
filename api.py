import os
from dotenv import load_dotenv, dotenv_values
import requests
from sys import argv

load_dotenv()
api = os.getenv("API_KEY")
site = os.getenv("URL")
# Replace 'API_KEY' with your actual API key 
def p1():
    API_KEY = f'{api}'
    tid = argv [1]
    url = f"{site}/api/v1/tasks/{tid}"
    head = {'Authorization': 'Bearer {}'.format(API_KEY)}
    headers = {'content-type': 'application/json'}
    response = requests.get(url, headers=head)
    print(response.status_code)
    print(response.json())
p1()
