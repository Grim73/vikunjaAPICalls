import os
from dotenv import load_dotenv, dotenv_values
import requests
from sys import argv

load_dotenv()
api = os.getenv("API_KEY")
site = os.getenv("URL")
def p1():
    API_KEY = f'{api}'
    #tid = argv [1]
    url = f"{site}/api/v1/projects"
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
        views = item['views']
        viewi = views[0]
        viewid = viewi['id']
        print(type(viewid))
        input('...')
        input("continue?")
        print(f"{title}.{taskid} \n {viewid}")
        input("continue?")
        for extract in views:

            idfin = extract['id']
            vkind = extract['view_kind']
            print(f"{idfin}  {vkind}")
        #    input("continue")

    #print(title)
    
p1()
