import requests

counter = 0

url = "https://movie.douban.com/j/chart/top_list?"

for i in range(100,0,-10):
    start = 0
    while (True):
        # get参数
        parameter = {
            "type":"24",
            "interval_id":str(i)+":"+str(i-10),
            "action":"",
            "start":start,
            "limit":"20",
        }
        start = start + 20
        result = requests.get(url,params=parameter).json()
        if(len(result) == 0):
            break
        for item in result:
            title = item["title"]
            score = item["score"]
            vote_count = item["vote_count"]
            counter = counter + 1
            print(counter,title,score,vote_count)


