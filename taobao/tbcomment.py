"""
获取淘宝链接评论
"""
import requests
import re
PAGE_URL = []  # 储存URL地址

def get_url(num):
    """定义一个生成链接列表函数"""
    urlfirst = ' https://rate.tmall.com/list_detail_rate.htm?itemId=610543532344&spuId=1502234835&sellerId=2416208484&order=3&currentPage='
    urllast = '&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvx9v7v7hvjQCkvvvvvjiWPLLOljrPRsqvgjivPmPZtj1RRFSUtji2PFFZ0ju%2BvpvEvvhjCEgv9V3MdvhvmpvCDXBmvU2FHTQCvvyvvLw0%2BpmvcfggvpvhvvCvp8QCvvyvvLQYVQmv7Z9VvpvEqYMwzHiDjynF39hvCvmvphvgvpvhvvCvpvvCvvOv9hCvvvvUvpCWvZIfV1llHd8rejUSYE7rVXeKfvVgQfutnCBAoYFWeCIXVcaHz8p7r3wgnZ43IEkZHdXKjrcnnCpXDVQEfwkXdiT7wxzEIEy7VBODNu9Cvv9vvhhtNl9PAU9CvvOCvhE2gRogvpvIvvCvpvvvvvvvvhNjvvmClvvvBGwvvvUwvvCj1Qvvv99vvhNjvvvmmvgCvvLMMQvvi9hvCvvvpZo%2BvpvEvU2UApOvvvWgRvhvCvvvphvVvpvEqYMwzH%2BoyZnFdvhvmpmvzaDYvUCDDIvCvCLNYsQGhxdNz%2Fa0TM1wn%2FJozTPw5L9CvvpvvhCvdvhvmpmCoy5JvUCu%2Bp%3D%3D&needFold=0&_ksTS=1618650592183_2356&callback=jsonp2357'
    for i in range(0,num):
        PAGE_URL.append(urlfirst + str(1+i) + urllast)

def getinfo(num):
    """定义字段"""
    name = []
    auctionSku = []
    ratecontent = []
    ratedate = []
    for i in range(num):
        # 定义头文件
        headers = {
            'cookie':'hng=CN|zh-CN|CNY|156; lid=takeoff2014; enc=uvHAMe5raCSfCkTvv094SCExvQXEUWOhnn/5D/lV0p2OlignjoFBBnjw7XbIySDwickBngwbMVY4tZ09kStCSw==; cna=mPrqGMBlxGECAToX/+4HQps1; xlly_s=1; _m_h5_tk=7e14e9f54f86a1aa9df2a9c4c0ac21f3_1618580756384; _m_h5_tk_enc=2f5ec2ff822e101b7f0beeeead8c3306; OZ_1U_2061=vid=v079780c7ffe82.0&ctime=1618573461&ltime=1618573459; dnk=takeoff2014; uc1=pas=0&cookie21=Vq8l+KCLjhS4UhJVbhgU&cookie16=W5iHLLyFPlMGbLDwA+dvAGZqLg==&existShop=false&cookie14=Uoe1iua6rgEDAg==&cookie15=Vq8l+KCLz3/65A==; uc3=vt3=F8dCuwpkhFMjHmWqIHg=&lg2=W5iHLLyFOGW7aA==&id2=UojTU5Wq1sQHiA==&nk2=F5fXdoAT4HtLInY=; tracknick=takeoff2014; uc4=nk4=0@FY0YPtzJ7eAW0ANzSCuzNTrBxKaNLA==&id4=0@UOBXUg9mXG79ZnMIh7TdovasesYE; _l_g_=Ug==; unb=1977370856; lgc=takeoff2014; cookie1=AHmCiL8Eoz74z7zG/SD6LT5IXooe9YR8KlZVYPmPpzQ=; login=true; cookie17=UojTU5Wq1sQHiA==; cookie2=1e0c81f7444c62d013a702deb5bbc347; _nk_=takeoff2014; sgcookie=E100KEq4rueVkd54cVtoarQ856gPjEtXFkt/CW9KKTel2gxLjMrou5NXs1LFoivoq9iuE3u1J0PcZwL1vfGsDvoyKA==; t=287c3dcde62dd1097b7be4f2f511193a; sg=462; csg=f2d70aa5; _tb_token_=f3e7a06778d3b; x5sec=7b22726174656d616e616765723b32223a226664326266316432666364316434613962656539663430663161653764333331434a376d366f4d474550486e6d59796c2b36664767514561444445354e7a637a4e7a41344e5459374d54447475662f632f762f2f2f2f3842227d; isg=BDEx_Ntx9boMw1m5o_kLoVsyQL3LHqWQb_nYxxNCMvncOlmMWmrYYDAcXM5c8j3I; tfstk=cd9GBuqakC56U41HNA66fW61T7-ca82VrKJBLK2JR7cW6Wv1bsfzT7uKHDbMSKFf.; l=eBEaHVePjHF6Z4TaBO5Znurza77O0CAfcsPzaNbMiIncC6yPizJTrPtQDAuUWLxRR8XVGYLp4JgP0zet3UG_JyTfoTB7K9cdvdpJQe8C.',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
            'referer':'https://detail.tmall.com/item.htm?id=610543532344',
            'accept':'*/*',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'zh-CN,zh;q=0.9'
        }
        # 解析js文件内容
        content = requests.get(PAGE_URL[i],headers=headers).text
        dk = re.findall('"displayUserNick":"(.*?)"', content)
        name.extend(dk)
        print(dk)
        # print(i)
        auctionSku.extend(re.findall('"auctionSku":"(.*?)"', content))
        ratecontent.extend(re.findall('"rateContent":"(.*?)"', content))
        ratedate.extend(re.findall('"rateDate":"(.*?)"', content))
    # 将数据写入text文件中
    for i in list(range(0, len(name))):
        text = ','.join((name[i], ratedate[i], auctionSku[i], ratecontent[i])) + '\n'
        with open(r"D:\content.txt", 'a+', encoding='UTF-8') as file:
            file.write(text + ' ')
            print(i + 1, "：写成功")


if __name__ == "__main__":
    """主函数"""
    page_num = 20
    get_url(page_num)
    getinfo(20)
