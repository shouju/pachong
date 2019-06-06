# chardet第三方库，
# 用来判断编码的模块
# 使用chardet.detect()方法，判断网页的编码方式
# 安装方法：pip install chardet

# urllib 内置url请求库 request请求模块
from urllib import request
# 做编码判断的第三方库
import chardet

# 定义访问的url
url = "http://www.baidu.com"
# 打开url
response = request.urlopen(url)
# <class 'http.client.HTTPResponse'> 服务器应答的数据包含在这个类里
print(type(response))
# 读取网页信息 返回bytes信息
result = response.read()
# 编码判断
detectResult = chardet.detect(result)
print(detectResult)
print(type(detectResult))
# 拿到网页编码
# 把bytes转化为str
html = result.decode(detectResult["encoding"])
print(html)

