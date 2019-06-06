from urllib import request

url = "http://ip.27399.com/"

# 构造一个字典传入一个代理地址
proxy = {"http":"110.185.52.141:8118"}
# 传递代理地址
proxyHandler = request.ProxyHandler(proxy)
# 构造urllib要求的urlopener打开器
opener = request.build_opener(proxyHandler)
# 进行安装
request.install_opener(opener)

req = request.Request(url)
htmlBytes = request.urlopen(req).read()
print(htmlBytes.decode())