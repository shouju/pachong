# urllib 的封装
import requests

url = "http://www.baidu.com/s?"

params = {"wd":"笔记本"}
headers = {
    "User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)"
}
# get == urllib.request.urlopen
response = requests.get(url,params=params,headers=headers)
# <Response [200]>
# <class 'requests.models.Response'>
print(response)
print(type(response))
# 获取字节数据 == read()
htmlBytes = response.content
# 解码
print(htmlBytes.decode())