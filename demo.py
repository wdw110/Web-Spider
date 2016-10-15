#encoding=utf-8

import urllib
import urllib2

'''
response = urllib2.urlopen('http://www.baidu.com')

#print response
#print response.read()

request = urllib2.Request('http://www.baidu.com') #构造request请求

response = urllib2.urlopen(request)

print response.read()


# Post方式传送
values = {'username':'1101627533@qq.com','password':'XXXXX'}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)

print response.read()

# Get方式传送
values = {'username':'1101627533@qq.com','password':'XXXXX'}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url+data)
response = urllib2.urlopen(request)

print response.read()

# urllib库应用
# 1.Headers的设置
url = 'http://www.server.com/login'
values = {'username':'wdw','password':'XXXXX'}
headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
                        'Referer':'http://www.zhihu.com/articles' } #加入referer对付’反盗链‘方式(服务器会识别 headers 中的 referer 是不是它自己，如果不是，有的服务器不会响应) 
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()

print page

# 2.Proxy的设置
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({'http': 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
	opener = urllib2.build_opener(proxy_handler)
else:
	opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

# 3.Timeout的设置
######如果第二个参数 data 为空那么要特别指定是 timeout 是多少，写明形参，
######如果data已经传入，则不必声明。
response = urllib2.urlopen('http://www.baidu.com',timeout=10)

# 4.使用HTTP的put和delete方法
#http 协议有六种请求方法，get,head,put,delete,post,options
#PUT：这个方法比较少见。HTML 表单也不支持这个。本质上来讲， PUT 和 POST 极为相似，
#都是向服务器发送数据，但它们之间有一个重要区别，PUT 通常指定了资源的存放位置，
#而 POST 则没有，POST 的数据存放位置由服务器自己决定。 
#DELETE：删除某一个资源。基本上这个也很少见，不过还是有一些地方比如amazon的S3云服务里面就用的这个方法来删除资源。 
#如果要使用 HTTP PUT 和 DELETE ，只能使用比较低层的 httplib 库。虽然如此，我们还是能通过下面的方式，
#使 urllib2 能够发出 PUT 或DELETE 的请求，不过用的次数的确是少，在这里提一下。
request = urllib2.Request(url, data)
request.get_method = lambda: 'PUT' # or 'DELETE'
response = urlib2.urlopen(request)

# 5.使用DebugLog
#可以通过下面的方法把 Debug Log 打开，这样收发包的内容就会在屏幕上打印出来，方便调试，这个也不太常用，仅提一下
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')


##URLError异常处理
request = urllib2.Request('http://wwww.xxxxx.com')
try:
	urllib2.urlopen(request)
except urllib2.URLError, e:
	print e.reason


##获取Cookie保存到变量
import cookielib

cookie = cookielib.CookieJar() #声明一个CookieJar对象实例来保存cookie
handler = urllib2.HTTPCookieProcessor(cookie) #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
opener = urllib2.build_opener(handler) #通过handler来构建opener
response = opener.open('http://www.baidu.com') #此处的open方法同urllib2的urlopen方法，也可以传入request
for item in cookie:
	print 'Name = '+item.name 
	print 'Value = '+item.value 	
'''

##保存Cookie到文件

import cookielib
import urllib2

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename) #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
handler = urllib2.HTTPCookieProcessor(cookie) #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
opener = urllib2.build_opener(handler) #通过handler来创建opener
response = opener.open('http://www.baidu.com') #创建一个请求，原理同urllib2的urlopen
cookie.save(ignore_discard=True, ignore_expires=True) #保存cookie到文件


##从文件中获取Cookie并访问
cookie = cookielib.MozillaCookieJar() #创建MozillaCookieJar实例对象
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True) #从文件中读取cookie内容到变量
req = urllib2.Request('http://www.baidu.com') #创建请求的request
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie)) #利用urllib2的build_opener方法创建一个opener
response = opener.open(req)
print response.read()

##
























