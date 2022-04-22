import requests

def getPage(url, dest, encoding):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
    }
    response = requests.get(url=url, headers=headers).content.decode(encoding=encoding)
    fw = open(dest, 'w', encoding='utf-8')
    fw.write(response)
    fw.close()
    return