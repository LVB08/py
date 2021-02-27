import requests
# import time
# from tqdm import tqdm
from bs4 import BeautifulSoup


def get_content(target):
    """获取小说单章内容"""
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    texts = bf.find('div', id='content')
    content = texts.text.strip().split('\xa0'*4)
    return content


if __name__ == '__main__':
    """主方法"""
    server = 'https://www.xsbiquge.com'
    book_name = '诡秘之主.txt'
    target = 'https://www.vbiquge.com/15_15338/'
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    bs = BeautifulSoup(html, 'lxml')
    chapters = bs.find('div', id='list')
    chapters = chapters.find_all('a')
    chap_num = 0
    for chapter in chapters:
        chap_num += 1
        chapter_name = chapter.string
        url = server + chapter.get('href')
        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')
        # 由于全部下载时间太长，所以设置只下载前100章
        if chap_num == 100:
            break

