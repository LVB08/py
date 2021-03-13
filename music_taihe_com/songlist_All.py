"""获取全部歌单名称"""
import requests
from bs4 import BeautifulSoup
from artist_nameAll import get_maxpageno
import re
from mySQLop import connection_insert


def get_songlist(arr, target):
    """获取单页所有歌单名称"""
    brr = []
    req = requests.get(url=target)
    html = req.text
    bs = BeautifulSoup(html, 'lxml')
    songlists = bs.select('div .name')
    for songlist in songlists:
        brr.append(songlist.string)
        crr = brr[:]
        arr.append(crr)
        brr.clear()
    return arr


if __name__ == '__main__':
    """主函数"""
    arr = []
    firsturl = 'https://music.taihe.com/songlist?subCateId=&pageNo=1'
    maxpageno = int(get_maxpageno(firsturl)) + 1
    for i in range(1,maxpageno):
        target = 'https://music.taihe.com/songlist?subCateId=&pageNo=' + str(i)
        arr = get_songlist(arr,target)
    print(len(arr))
    insert_sql = """insert into songlist_info (name) values (%s)"""
    connection_insert(insert_sql,arr)
