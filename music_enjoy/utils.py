import requests
from bs4 import BeautifulSoup
import json

DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'

DEFAULT_HEADERS = {
    'User-Agent': DEFAULT_USER_AGENT,
}


def get_page(url, headers=DEFAULT_HEADERS, encoding='utf-8'):
    response = requests.get(url=url, headers=headers)
    print(response.status_code)
    content = response.content.decode(encoding=encoding)
    return content


def download(url, dest, headers=DEFAULT_HEADERS):
    try:
        response = requests.get(url=url, headers=headers,
                                stream=True, verify=True)
        print(response.status_code)
        with open(dest, 'wb') as fw:
            for chunk in response.iter_content(1024):
                fw.write(chunk)
                fw.flush()  # 清空缓存
    except Exception as e:
        print("url下载错误: %s" % url)
        print(e)
    return


def bilibili(url, dest, audio_or_video):
    headers = {
        'User-Agent': DEFAULT_USER_AGENT,
        "Origin": 'https://www.bilibili.com/',
        "Referer": 'https://www.bilibili.com/',
    }
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    video_url = ''
    audio_rul = ''
    for i in range(len(soup('script'))):
        pattern = 'window.__playinfo__='
        if str(soup('script')[i].string)[:len(pattern)] == pattern:
            info = str(soup('script')[i].string)[len(pattern):]
            info_dict = json.loads(info)
            video_url = info_dict['data']['dash']['video'][0]['baseUrl']
            audio_rul = info_dict['data']['dash']['audio'][0]['baseUrl']
            break
    if audio_or_video == 'audio':
        download(url=audio_rul,dest=dest,headers=headers)
    if audio_or_video == 'video':
        download(url=video_url,dest=dest,headers=headers)
    return


if __name__ == '__main__':
    url = 'https://www.bilibili.com/video/BV1C7411q7WV/?spm_id_from=autoNext'
    bilibili(url=url, dest='./1.mp4', audio_or_video='audio')
    pass
