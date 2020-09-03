from bs4 import BeautifulSoup
import requests
url='https://bj.lianjia.com/zufang'
res=requests.get(url)
print(res)
#print(res.text)

soup=BeautifulSoup(res.text,'html.parser')

links_div = soup.find_all('div',class_="content__list--item")

links = [div.a.get('href') for div in links_div]
print(links,len(links))


def get_links(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    links_div = soup.find_all('div', class_="content__list--item")

    links = [div.a.get('href') for div in links_div]
    return links

def get_page(url):
    reponse=requests.get(url)
    return BeautifulSoup(reponse.text,'html.parser')

house_url = 'https://bj.lianjia.com/zufang/BJ2538554511837110272.html'
soup =get_page(house_url)

#获取价格
price = soup.find('div',class_="content__aside--title").span.text
print(price)
ul_info =soup.find_all('ul',class_="content__aside__list")
print(ul_info[0].li.span.text)
#content__article__info
#base_info =soup.find_all('div',id="info").ul
base_info =soup.select('div.content__article__info >ul li')
#print(base_info)
print(len(base_info))
info_in ={}
'''
for info in base_info:
    if (info.text !='' and info.text !=None):
        print(info.text)
        arr=info.text.split("：")
        print(arr[0])
'''
HOUSE_INFO={
    '面积':base_info[1].text.split("：")[1]
}
print(HOUSE_INFO)

