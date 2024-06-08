import os
from dotenv import load_dotenv, dotenv_values
import requests
from sys import argv

load_dotenv()
api = os.getenv("API_KEY")
site = os.getenv("URL")
# Replace 'API_KEY' with your actual API key from NewsAPI
def p1():
    API_KEY = f'{api}'
    url = f"{site}/api/v1/projects/-16/views/129/tasks"
    head = {'Authorization': 'Bearer {}'.format(API_KEY)}
    headers = {'content-type': 'application/json'}
    response = requests.get(url, headers=head)
    output = response.json()
    paired = output[0]
    title = paired["title"]

    for item in output:
        title = item['title']
        taskid = item['id']
        print(title,".",taskid)
        #for extract in item:
        #    print(type(extract))
        #    input("continue")

    print(title)
 
p1()
