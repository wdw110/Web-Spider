#encoding=utf-8

import re
import urllib
import urllib2
import cookielib
import webbrowser
import tool_taobao

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
		#赋值J_HToken
		self.J_HToken = ''
		#登录成功时，需要的Cookie
		self.newCookie = cookielib.CookieJar()
		#登陆成功时，需要的一个新的opener
		self.newOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.newCookie))
		#引入工具类
		self.tool = tool_taobao.Tool()

	#得到是否需要输入验证码，这次请求的相应有时会不同，有时需要用验证码又是不需要
	def needCheckCode(self):
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

	#得到验证码
	def getCheckCode(self,page):
		pattern = re.compile('<img id="J_StandardCode_m.*?data-src="(.*?)"',re.S) #得到验证码的图片
		matchResult = re.search(pattern,page) #匹配的结果
		if matchResult and matchResult.group(1): #已经匹配得到内容，并且验证码连接不为空
			print matchResult.group(1)
			return matchResult.group(1)
		else:
			print u'没有找到验证码内容'
			return False

	#输入验证码，重新请求，如果验证成功，则返回J_HToken
	def loginWithCheckCode(self):
		#提示用户输入验证码
		checkcode = raw_input('请输入验证码:')
		#将验证码重新添加到post的数据中
		self.post['TPL_checkcode'] = checkcode
		#对post数据重新进行编码
		self.postData = urllib.urlencode(self.post)
		try:
			#再次构建请求，加入验证码之后的第二次登录尝试
			request = urllib2.Request(self.loginURL,self.postData,self.loginHeaders)
			#得到第一次登录尝试的相应
			response = self.opener.open(request)
			#获取其中的内容
			content = response.read().decode('gbk')
			#检测验证码错误的正则表达式，\u9a8c\u8bc1\u7801\u9519\u8bef 是验证码错误五个字的编码
			pattern = re.compile(u'\u9a8c\u8bc1\u7801\u9519\u8bef',re.S)
			result = re.search(pattern,content)
			#如果返回页面包括了，验证码错误五个字
			if result:
				print u"验证码输入错误"
				return False
			else:
				#返回结果直接带有J_HToken字样，说明验证码输入成功，成功跳转到了获取HToken的界面
				tokenPattern = re.compile('id="J_HToken" value="(.*?)"')
				tokenMatch = re.search(tokenPattern,content)
				#如果匹配成功，找到了J_HToken
				if tokenMatch:
					print u"验证码输入正确"
					self.J_HToken = tokenMatch.group(1)
					return tokenMatch.group(1)
				else:
					#匹配失败，J_Token获取失败
					print u"J_Token获取失败"
					return False
		except urllib2.HTTPError, e:
			print u"连接服务器出错，错误原因",e.reason
			return False

	def getSTbyToken(self,token):
		tokenURL = 'https://passport.alipay.com/mini_apply_st.js?site=0&token=%s&callback=stCallback6' % token
		request = urllib2.Request(tokenURL)
		response = urllib2.urlopen(request)
		pettern = re.compile('{"st":"(.*?)"}',re.S) #处理st,获得用户淘宝主页登陆地址
		result = re.search(pattern,response,read())
		if result:
			print u'成功获取st码'
			st = result.group(1)
			return st 
		else:
			print u'未匹配到st'
			return False

	#利用st码进行登录,获取重定向网址
	def loginByST(self,st,username):
		stURL = 'https://login.taobao.com/member/vst.htm?st=%s&TPL_username=%s' % (st,username)
		headers = {
			'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
			'Host':'login.taobao.com',
			'Connection' : 'Keep-Alive'
		}
		request = urllib2.Request(stURL,headers = headers)
		response = self.newOpener.open(request)
		content =  response.read().decode('gbk')
		#检测结果，看是否登录成功
		pattern = re.compile('top.location = "(.*?)"',re.S)
		match = re.search(pattern,content)
		if match:
			print u"登录网址成功"
			location = match.group(1)
			return True
		else:
			print "登录失败"
			return False

	#获取已买到的宝贝页面
	def getGoodspage(self,pageIndex):
		goodsURL = 'http://buyer.trade.taobao.com/trade/itemlist/listBoughtItems.htm?action=itemlist/QueryAction&event_submit_do_query=1&pageNum=' + str(pageIndex)
		response = self.newOpener.open(goodsURL)
		page = response.read().decode('gbk')
		return page

	#获取所有已买到的宝贝信息
	def getAllGoods(self,pageNum):
		print u"获取到的商品列表如下"
		for x in range(1,int(pageNum)+1):
			page = self.getGoodsPage(x)
			self.tool.getGoodsInfo(page)

	def main(self): #主程序代码
		needResult = self.needCheckCode()
		if not needResult == None:
			if not needResult == False:
				print u'你需要手动输入验证码'
				idenCode = self.getCheckCode(needResult)
				if not idenCode == False: #得到了验证码的链接
					print u'验证码获取成功'
					print u'请在浏览器中输入验证码'
					webbrowser.open_new_tab(idenCode)
					self.loginWithCheckCode()
					#print 'J_HToken',J_HToken
				else:
					print u'验证码获取失败，请重试'
			else:
				print u'不需要输入验证码'
		else:
			print u'请求登录页面失败，无法确认是否需要验证码'

		#判断token是否正常获取到
		if not self.J_HToken:
			print "获取Token失败，请重试"
			return
		#获取st码
		st = self.getSTbyToken(self.J_HToken)
		#利用st进行登录
		result = self.loginByST(st,self.username)
		if result:
			#获得所有宝贝的页面
			page = self.getGoodsPage(1)
			pageNum = self.tool.getPageNum(page)
			self.getAllGoods(pageNum)
		else:
			print u"登录失败"

b = Taobao()
b.main()

