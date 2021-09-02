import requests
import json
import os
import re

def download(url:str, file:str):
        r = requests.get(url, stream=True)

        if r.status_code == 200:
            with open(file, 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
            f.close()

def fetch(file:str, id:str):
    '''
    Fetch all costumes and sounds used in a project
    '''
    os.chdir(os.getcwd())

    if not os.path.exists('./assets'):
        os.mkdir('./assets')

    r = requests.get('https://projects.scratch.mit.edu/{}'.format(id), stream=True)

    if r.status_code == 200:
        with open(file+'.json', 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
        f.close()
    else:
        return requests.exceptions.RequestException

    with open(file+'.json', 'r') as f:
        JSON = json.loads(f.read())
    f.close()

    i = 0
    while True:
        try:
            cst = JSON['targets'][i]['costumes'][0]
            name = JSON['targets'][i]['name']
            fld = './assets/'+re.sub('[^\w\-_\. ]', '_', name)

            try:
                os.mkdir(fld)
            except FileExistsError:
                pass

            r = download('https://cdn.assets.scratch.mit.edu/internalapi/asset/{}/get'.format(cst['md5ext']), fld+'/'+cst['name']+'.'+cst['dataFormat'])

            i += 1
        except IndexError:
            break
    
    i = 0
    while True:
        try:
            snd = JSON['targets'][i]['sounds'][0]
            name = JSON['targets'][i]['name']
            fld = './assets/'+re.sub('[^\w\-_\. ]', '_', name)

            try:
                os.mkdir(fld)
            except FileExistsError:
                pass

            r = download('https://cdn.assets.scratch.mit.edu/internalapi/asset/{}/get'.format(snd['md5ext']), fld+'/'+snd['name']+'.'+snd['dataFormat'])

            i += 1
        except IndexError:
            break
    
    os.remove('./project.json')