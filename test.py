import requests
from bs4 import BeautifulSoup


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


if __name__  == '__main__':
    print(get_selValue()[0])
    print(get_selValue()[1])
    print(get_selValue()[2])