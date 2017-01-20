#encoding=utf-8

import urllib2
import requests

response = urllib2.urlopen('http://www.baidu.com/')
html = response.read()

req = urllib2.Request('http://www.baidu.com')
res = urllib2.urlopen(req)
the_page = res.read()
#print the_page

url = 'http://www.baidu.com'
r = requests.get(url)
print type(r)
print r.status_code
print r.encoding
#print r.text
print r.cookies

payload = {'key1':'value1','key2':'value2'}
headers = {'content-type':'application/json'}
r = requests.get(url, params=payload, headers=headers)
print r.url

#r = requests.get('https://github.com/timeline.json', stream=True)
#print r.raw

r = requests.post('http://httpbin.org/post', data=payload)
print r.text

r = requests.get(url)
print r.cookies
#print r.cookies['BDORZ']

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print r.text

r = requests.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
print r.text
r = requests.get('http://httpbin.org/cookies')
print r.text

s = requests.Session()
s.headers.update({'x-test':'true'})
r = s.get('http://httpbin.org/headers',headers={'x-test2':'true'})
print r.text

#r = requests.get('https://kyfw.12306.cn/otn', verify=False) #如果我们想跳过刚才12306的证书验证，把 verify 设置为 False 即可
#print r.text

#r = requests.get('https://github.com', verify=True)
#print r.text

proxies = {'https':'http://41.118.132.69:4433'}
r = requests.post('http://httpbin.org/post', proxies=proxies)
print r.text

export HTTP_PROXY = 'http://10.10.1.10:3128'
export HTTPS_PROXY = 'http://10.10.1.10:1080'
