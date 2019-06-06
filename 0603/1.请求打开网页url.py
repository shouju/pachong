# urllib.request.urlopen()
# 这个接口函数可以很轻松的打开一个网站。读取并打印信息。

# urllib 内置url请求库 request请求模块
from urllib import request

# 定义访问的url
url = "http://www.baidu.com"
# 打开url
response = request.urlopen(url)
# <class 'http.client.HTTPResponse'> 服务器应答的数据包含在这个类里
print(type(response))
# 读取网页信息 返回bytes信息
result = response.read()
print(result)
print(type(result))
# 把bytes转化为str
html = result.decode()
print(html)
print(type(html))