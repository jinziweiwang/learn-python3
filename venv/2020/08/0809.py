#模拟浏览器请求的库
import requests
#模拟正则的库
import re
#url = 'https://www.goodreads.cc'
url = 'https://www.baidu.com'
header ={
    'user-agent':'Mozlila/5.0'
}
res =requests.get(url)
print(res.text)
#正则表达式
parten = '<h2/><a href="(.*?)"></a></h2>'
result = re.findall(pattern=parten,string=res.text)
print(result)

