from urllib import request
from urllib import parse
import time

def DownLoad(start,end,name):
    index = 0
    print(start,end,name)
    for i in range((start-1)*50,(end-1)*50+1,50):
        index = index + 1
        #构造参数
        params = {
            "kw":name,
            "ie":"utf-8",
            "pn":i,
        }
        #转换成url格式
        params = parse.urlencode(params)
        #构造url
        url = "https://tieba.baidu.com/f?" + params
        print(url)
        #构造请求对象
        req = request.Request(url)
        #获取页面二进制信息
        html = request.urlopen(req).read()
        #写入本地
        with open("./" + str(index) + ".html",'wb') as f:
            f.write(html)
        time.sleep(2)

DownLoad(1,5,"手机")
