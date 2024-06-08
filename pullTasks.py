import os
from dotenv import load_dotenv, dotenv_values
import requests
from sys import argv

load_dotenv()
api = os.getenv("API_KEY")
site = os.getenv("URL")
pid = argv[1]
vid = argv[2]
# Replace 'API_KEY' with your actual API key from NewsAPI
def p1():
    API_KEY = f'{api}'
    url = f"{site}/api/v1/projects/{pid}/views/{vid}/tasks"
    head = {'Authorization': 'Bearer {}'.format(API_KEY)}
    headers = {'content-type': 'application/json'}
    response = requests.get(url, headers=head)
    #print(response.status_code)
    #print(response.json())

    output = response.json()
    paired = output[0]
    title = paired["title"]

    for item in output:
        title = item['title']
        taskid = item['id']
        #input()
        print(f"{title}.{taskid}")
        #for extract in item:
        #    print(type(extract))
        #    input("continue")

    #print(title)
    
p1()
