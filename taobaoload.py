#encoding=utf-8

import re
import urllib
import urllib2
import cookielib
import webbrowser

#模拟淘宝登录类
class Taobao(object):
	"""docstring for Taobao"""
	def __init__(self):
		self.loginURL = "https://login.taobao.com/member/login.jhtml"  #登陆URL
		self.proxyURL = 'http://120.193.146.97:843'   #代理IP地址，防止自己IP被封
		self.loginHeaders =  {'Host':'login.taobao.com','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0','Referer':'https://login.taobao.com/member/login.jhtml','Content-Type':'application/x-www-form-urlencoded','Connection':'Keep-Alive'}

		self.username = '15958149403'
		self.ua = '082#b3SkffkYWVGkTUWOkkkkkTVKAUfcT67HczxtkKtZC6puJgTrBhYlYTBwAwwnDgslUjONNN/f8MerJTkwBEQlCTuFAUFnIAIWkWudAeI5ke7/TmEmYFM2M7HTnzYKstGrkqkFXjocbfNHWhsZL6ROd7HlNI5xG9nbwUSkwsxNPn0kXNq9vev8/8HlMfcbc8TZn4IWkWudEpI5kifmTmEmYFM2M7HTnzYKstGrkqkFXjycbfQiPNsZL6ROd7HlNI5xG9nbwUSkwsxBPn0kTwS9vev8/8HlMfcbc8TZnIqWkWO4cKRHT3gDFzB1KW+1C5Td+l3duIqWkWO4cNRHbPzDFzB1KW+1C5Td+l3duIqWkWO4cKRHSIzDFzB1KW+1C5Td+l3duKqWkk4nDVWflkSkQsmpOJHiHubQrNqWkk4nDVWf5USk1R0/JkNvo1Lur4iBkaSEevtfzgYiYkUBZhWclkSkwyhp/wk3HubBwNUE0RoISOSUqqA8FgU4QkSkWByphiZfkqk/pmPKSwHLjDNIdRWCa3uQOjz0V5vYkqktG0tUQ7Y/ynMIkqk1suE7+GnEnkSkMS3Gd2kX2JAAK1OxPhRpO4CiDb6DBrPaq/3G58GX2JYGK1OzdNRpOYqQkqS/+/wmEqIQc6vQvwKQkA5tjDL3NZfWwi6A9mf/USS27YsKPU5QkA5tjDL3SI/x1+e+UpIQUqgafYvoPAYWkRNW8t2aSjiV4badUyIs7fUNf6Lv9W6bWfKMYIrZNX+2SZdpULIoAWfKhanGPEoqWUa2YZM5OzAzTZYZ3eIP7w3N5zv16qdWQRE2v8m+1jbkw0QgCBDB97AqfYvoPUviVWsOjP9HFP3tSTc75MSiUAfx76ssL4MNWUa2YZMZFitD1zc3R2HeEkS/hYVopWOkq4pBpblyNXXWw+Bp9lt/nU0IGBM/+WMoQ3u2EYep4j/xkgLHCBDB9nPK5xENAFmorJK858mHwZRkkH6AGyt/ffJDfvoNPGdldUSkWUkW3m1pOKqWkk4nDVWfMUSkVZdbNJXUIjrJCeq3iQ+fRDB7yJbktKBIG2s2iQfhiD7HkqkuyB++eNx30GXIBQT7FPU4tOWWQ1RrcW1Skqk/GzUX2WNKrFuKAGfoWgDhDpM+DRcHkqkuyB+yehs30G7xBQTfFgk1tCSUaFAaJAdHkqkuyB61A5c30GM2qn3Uo0qWacW0VuWVmGirkqkFXvhJbfQjsNsZL6ROd7HlNI5xG9nbwUSkwsxRPn0kYVf9vev8/8HlMfcbc8TZnKqWkk4nDVWf5USkNwGFcqQxo1LurrCHkNqWkk4nDVWfAkSkwbVIBrf9rCRFJZDiVf2r0c27p1DzwUSkwsx1Pn0k+7Z9vev8/8HlMfcbc8TZnKqWkk4nDVWfwUSkwsxQPn0kWQi9vev8/8HlMfcbc8TZn4IWkWudUpI5kV74TmEmYFM2M7HTnzYKstGrkqkFXj2cbfQ0NhsZL6ROd7HlNI5xG9nbwUSkwsxNPn0kpS/9vev8/8HlMfcbc8TZnDZWkW8uwz/k/93pRCdfbUQpaQetMuK09tfKVoi1bNqWkk4nDVWfAkSkwbVDBrfMYFRFJZDiVf2r0c27p1Dz'
		#ua字符串，经过淘宝ua算法计算得出，包含了时间戳,浏览器,屏幕分辨率,随机数,鼠标移动,鼠标点击,其实还有键盘输入记录,鼠标移动的记录、点击的记录等等的信息
		self.password2 = '5c586fe45ccae599f4215726ee15b3cec27ab5f78b6c1f2df17a80564db1c94389b771fe33128631151869154982481d203286bae840387ac127f1462e0834d440255b12173c9c08a012e0ac32877253380b26644725a037d5ad8416c2a56ab0788a6b392ae6b6d39a6863a1d3472ab4e1f060ac7b14759c9e37c4c13703db7e'
		#密码，在这里不能输入真实密码，淘宝对此密码进行了加密处理，256位，此处为加密后的密码
		self.post = post = {
				'ua':self.ua,
				'TPL_checkcode':'',
				'CtrlVersion': '1,0,0,7',
				'TPL_password':'',
				'TPL_redirect_url':'http://i.taobao.com/my_taobao.htm?nekot=udm8087E1424147022443',
				'TPL_username':self.username,
				'loginsite':'0',
				'newlogin':'0',
				'from':'tb',
				'fc':'default',
				'style':'default',
				'css_style':'',
				'tid':'XOR_1_000000000000000000000000000000_625C4720470A0A050976770A',
				'support':'000001',
				'loginType':'4',
				'minititle':'',
				'minipara':'',
				'umto':'NaN',
				'pstrong':'3',
				'llnick':'',
				'sign':'',
				'need_sign':'',
				'isIgnore':'',
				'full_redirect':'',
				'popid':'',
				'callback':'',
				'guf':'',
				'not_duplite_str':'',
				'need_user_id':'',
				'poy':'',
				'gvfdcname':'10',
				'gvfdcre':'',
				'from_encoding ':'',
				'sub':'',
				'TPL_password_2':self.password2,
				'loginASR':'1',
				'loginASRSuc':'1',
				'allp':'',
				'oslanguage':'zh-CN',
				'sr':'1366*768',
				'osVer':'windows|6.1',
				'naviVer':'firefox|35'
			}	

		self.postData = urllib.urlencode(self.post)
		self.proxy = urllib2.ProxyHandler({'http':self.proxyURL}) #设置代理
		self.cookie = cookielib.LWPCookieJar()  #设置cookie
		self.cookieHandler = urllib2.HTTPCookieProcessor(self.cookie) #设置cookie处理器
		self.opener = urllib2.build_opener(self.cookieHandler,self.proxy,urllib2.HTTPHandler)  #设置登录时用到的opener，它的open方法相当于urllib2.urlopen

	#得到是否需要输入验证码，这次请求的相应有时会不同，有时需要用验证码又是不需要
	def needIdenCode(self):
		request = urllib2.Request(self.loginURL,self.postData,self.loginHeaders)  #第一次登录获取验证码尝试，构建request
		response = self.opener.open(request)  #得到第一次登录尝试的相应
		content = response.read().decode('gbk')  #获取其中的内容
		status = response.getcode()  #获取状态码
		if status == 200:
			print u'获取请求成功'
			#\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801这六个字是请输入验证码的utf-8编码
			pattern = re.compile(u'\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801',re.S)
			result = re.search(pattern,content)
			#如果找到该消息，代表需要输入验证码
			if result:
				print u'此次安全验证异常，请输入验证码'
				return content
			else:
				print u'此次安全验证通过，您这次不需要输入验证码'
				return False
		else:
			print u'获取请求失败'


b = Taobao()
b.needIdenCode()

