import requests, os, pickle as pkl
def updatelocal():
    url = 'https://api.github.com/users/AmirMEdris/repos'
    r = requests.get(url)
    urls = []
    for item in r.json():
        urls.append((item['clone_url'],item['name']))
        os.system('git clone {}'.format(item['clone_url']))
        os.system('cd ..')
    return urls
print('do you want to update local files')
x = input('Y|N: ')
if x.upper() == 'Y':
    x = updatelocal()
    save = pkl.dump(x,open( "x.p", "wb" ))



