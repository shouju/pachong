from urllib import parse,request
from urllib.error import URLError,HTTPError
import json

# 有道翻译url
url = "htttps://movie.douban.com/j/chart/top_list?"
# get参数
parameter = {
    "type":"24",
    "interval_id":"100:90",
    "action":"unwatched",
    "start":"0",
    "limit":"20",
}

# get的参数直接拼接到url
url = url + parse.urlencode(parameter)
print(url)

# 捕捉异常
try:
    res = request.urlopen(url).read().decode()
    print(res)
    # <class 'str'>
    print(type(res))
except URLError as e:
    if(hasattr(e,"code")):
        print("http error" + str(e.code))
    if(hasattr(e,"reason")):
        print("url error"+ e.reason)

# # 拿到的是json字符串，把字符串转化为python对象 dict,list
# pythonObj = json.loads(res)
# print(pythonObj)
# print(type(pythonObj))
# for data in pythonObj:
#     print(data["title"])
