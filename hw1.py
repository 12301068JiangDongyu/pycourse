#获取百度检索自己名字的第 一页所有网页标题及链接
import re 
import requests  
from pyquery import PyQuery as pq

key_word = { 'wd' : '姜栋煜'}
response = requests.get("http://www.baidu.com/s?",params=key_word)
html = pq(response.text)
print('---------------------------------------------')

for res_item in html('#content_left h3.t a').items():
  print('标题：'+res_item.text())
  print('链接：'+res_item.attr('href'))
  print('---------------------------------------------')

