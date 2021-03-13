import requests
from bs4 import BeautifulSoup
from music_taihe_com.artist_detailed import get_single
from music_taihe_com.mySQLop import connection_insert


def get_maxpageno(target):
    """获取最大页数"""
    arr = []
    # target = 'https://music.taihe.com/artist?pageNo=1&artistFristLetter=&artistRegion=&artistGender='
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    bs = BeautifulSoup(html, 'lxml')
    sels = bs.select('div .el-pagination ul li')
    return sels[-1].string


if __name__ == '__main__':
    """只获取名称，并写入数据库"""
    insert_sql = ''
    firsturl = 'https://music.taihe.com/artist?pageNo=1&artistFristLetter=&artistRegion=&artistGender='
    maxpageno = int(get_maxpageno(firsturl)) + 1
    print(maxpageno)
    arr = []
    for i in range(1,maxpageno):
        target = 'https://music.taihe.com/artist?pageNo=' + str(i) + '&artistFristLetter=&artistRegion=&artistGender='
        req = requests.get(url=target)
        req.encoding = 'utf-8'
        html = req.text
        bs = BeautifulSoup(html, 'lxml')
        arr = get_single(arr,target,'','','','')
    print(len(arr))
    # 插入数据格式：[['歌手','邓紫棋1','女','大陆','D'],['歌手','邓紫棋2','女','大陆','D'],['歌手','邓紫棋3','女','大陆','D']]
    insert_sql = """insert into singer_info (type,name,gender,area,initials) 
                        values (%s,%s,%s,%s,%s)"""
    connection_insert(insert_sql,arr)
