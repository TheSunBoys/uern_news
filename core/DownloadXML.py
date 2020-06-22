import urllib.request

def downloadXML(urls, directory='.database'):
    print('[RSS] Baixando xmls ...') # log

    filenames = []
    failedUrls = []

    # dowload sem user-agent
    for x in range(len(urls)):
        try:
            urllib.request.urlretrieve(urls[x], f'{directory}/file{x}.xml')
            filenames.append(f'{directory}/file{x}.xml')
        except:
            print(f'[RSS] erro ao tentar baixar da url {urls[x]}, entando novamente com user-agent definido') # log
            failedUrls.append(urls[x])

    # donwload com user-agent
    if len(failedUrls) > 0:
        client = urllib.request.build_opener()
        client.addheaders = [(
            'User-agent',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
        )] # User Agent
        urllib.request.install_opener(client)
    
        for x1 in range(len(failedUrls)):
            try:
                urllib.request.urlretrieve(failedUrls[x1], f'{directory}/file{x+x1}.xml')
                filenames.append(f'{directory}/file{x+x1}.xml')
            except:
                print(f'[RSS] erro ao tentar baixar da url {urls[i]}') # log

    return filenames
