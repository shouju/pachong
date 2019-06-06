from urllib import parse,request

# https://www.baidu.com/s?wd=端午节
url = "http://www.baidu.com/s?"

paramDic ={
    "wd":"端午节"
}
# 将字典转化为url 需要的参数格式
subUrl = parse.urlencode(paramDic)
# 地址 + 参数
url = url + subUrl
print(url)

# 打开url
response = request.urlopen(url)
# <class 'http.client.HTTPResponse'> 服务器应答的数据包含在这个类里
print(type(response))
# 读取网页信息 返回bytes信息
result = response.read()
# 把bytes转化为str
html = result.decode()
print(html)

