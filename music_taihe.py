import requests
from bs4 import BeautifulSoup
from mySQLop import connection_sql

def get_selValue():
    """获取选择项信息如：首字母、地区、乐队&组合"""
    drr = []
    err = []
    frr = []
    target = 'https://music.taihe.com/artist'
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    bs = BeautifulSoup(html, 'lxml')
    sels = bs.select('div .filter-box ul')
    for sel in sels:
        for ss in sel:
            if ss.string == '全部':
                continue
            drr.append(ss.string)
        err = drr[:]
        frr.append(err)
        drr.clear()
    return frr

def get_pageno(target):
    """获取页数信息"""
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    no_html = req.text
    nobs = BeautifulSoup(no_html, 'lxml')
    nostrs = nobs.select('div .el-pagination ul li')
    pageno = len(nostrs)
    # 如果只有一页的情况，页面底部没有页数信息，所以需要赋值
    if pageno == 0:
        pageno = 1
    return pageno


def get_single(arr,target,typeValue,genderValue,areaValue,initialsV):
    """获取单页所有歌手信息"""
    brr = []
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    art_html = req.text
    artbs =BeautifulSoup(art_html, 'lxml')
    artists = artbs.select('div .name')
    artists = artists + artbs.select('div .list-item')
    for artist in artists:
        # arr.append(artist.string)
        brr.append(typeValue)
        brr.append(artist.string)
        brr.append(genderValue)
        brr.append(areaValue)
        brr.append(initialsV)
        crr = brr[:]
        arr.append(crr)
        brr.clear()
    return arr


if __name__ == '__main__':
    """获取百度音乐歌手信息"""
    initials = get_selValue()[0]
    region = get_selValue()[1]
    gender = get_selValue()[2]
    arr = []
    for x in region:  # 遍历地区
        areaValue = x
        for y in gender:  # 遍历类型
            if y == '男' or y == '女':
                typeValue = '歌手'
                genderValue = y
            else:
                typeValue = y
                genderValue = ''
            for z in initials:  # 遍历首字母
                initialsV = z
                noUrl = 'https://music.taihe.com/artist?pageNo=1&artistFristLetter=' + z + '&artistRegion=' + x + '&artistGender=' + y
                # sss = get_pageno(noUrl) + 1
                for i in range(1, get_pageno(noUrl) + 1):
                    Url = 'https://music.taihe.com/artist?pageNo=' + str(i) + '&artistFristLetter=' + z + '&artistRegion=' + x + '&artistGender=' + y
                    arr = get_single(arr, Url, typeValue, genderValue, areaValue, initialsV)
    print(len(arr))
    connection_sql(arr)





