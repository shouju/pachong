from urllib import request
import random

# 构造list
uaList = []
# 读取配置
with open("./UAConfig.txt") as cfg:
    data = cfg.read()
    # 分割之后拿到每一行数据
    lines = data.split("\n")
    for ua in lines:
        print(ua)

# 随机
userAgent = random.choice(lines)

print(len(lines))
print(userAgent)

# url = "http://www.baidu.com/"
# headers = {
#     "User-Agent":userAgent
# }
# # 声明请求对象的时候 注入请求头 修改User-Agent(身份)
# req = request.Request(url,headers=headers)
# # 网页请求
# html = request.urlopen(req).read()
# print(html.decode())