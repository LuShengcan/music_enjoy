import os
import requests





def download():
    if not os.path.exists('video-audio'):
        os.mkdir('video-audio')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
        "Origin": 'https://www.bilibili.com',
        "Referer": 'https://www.bilibili.com/video/BV1ki4y1d7Ln'
    }

    urls = ['https://cn-tj-fx-bcache-03.bilivideo.com/upgcxcode/90/53/459565390/459565390-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1649858333&gen=playurlv2&os=bcache&oi=3396451638&trid=0000810d3faaf6714ca0a80961752d0794b4u&platform=pc&upsig=26376f01cd389578f5ea11c949641d8c&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&cdnid=69903&mid=0&bvc=vod&nettype=0&orderid=0,3&agrr=0&bw=16279&logo=80000000']

    for i, url in enumerate(urls):
        try:
            response = requests.get(url, headers=headers,
                                    stream=True, verify=True)
            print(response.status_code)
            fileName = os.path.join('video-audio', "{}.m4a".format(i))
            with open(fileName, 'wb') as fw:
                for chunk in response.iter_content(1024):
                    fw.write(chunk)
                    fw.flush()  # 清空缓存
        except Exception as e:
            print("url下载错误：%s" % url)
            print(e)

    return


if __name__ == '__main__':

    # use
    # getPage(url='https://www.bilibili.com/video/BV1ki4y1d7Ln', pageName='pian-ai.html')
    download()
