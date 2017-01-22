#encoding=utf-8

import re

#处理页面标签类
class Tool():
	"""docstring for Tool"""
	#将超链接广告剔除
	removeADLink = re.compile('<div class="link_layer.*?</div>')
	#去除img标签，1-7位空格，&nbsp;
	removeImg = re.compile('<img.*?>| {1,7}|&nbsp;')
	#删除超链接标签
	removeAddr = re.compile('<a.*?>|</a>')
	#把换行的标签换为\n
	replaceLine = re.compile('<tr>|<div>|</div></p>')
	#将表格制表<td>替换为\t
	replaceTD = re.compile('<td>')
	#将换行符或双换行符替换为\n
	replaceBR = re.compile('<br><br>|<br>')
	#将其余标签剔除
	removeExtraTag = re.compile('<.*?>')
	#将多行空行删除
	removeNoneLine = re.compile('\n+')

	def replace(self,x):
		x = re.sub(self.removeADLink,"",x)
		x = re.sub(self.removeImg,"",x)
		x = re.sub(self.removeAddr,"",x)
		x = re.sub(self.replaceLine,"\n",x)
		x = re.sub(self.replaceTD,"\t",x)
		x = re.sub(self.replaceBR,"\n",x)
		x = re.sub(self.removeExtraTag,"",x)
		x = re.sub(self.removeNoneLine,"\n",x)
		#strip()将前后多余内容删除
		return x.strip()

	def test(self,content):
		return self.replace(content)


if __name__ == '__main__':
	a='''
<article class="article-content">
<h2>前言</h2>
<p>最近发现MySQL服务隔三差五就会挂掉，导致我的网站和爬虫都无法正常运作。自己的网站是基于MySQL，在做爬虫存取一些资料的时候也是基于MySQL，数据量一大了，MySQL它就有点受不了了，时不时会崩掉，虽然我自己有网站监控和邮件通知，但是好多时候还是需要我来手动连接我的服务器重新启动一下我的MySQL，这样简直太不友好了，所以，我就觉定自己写个脚本，定时监控它，如果发现它挂掉了就重启它。</p>
<p>好了，闲言碎语不多讲，开始我们的配置之旅。</p>
<p>运行环境：<strong>Ubuntu Linux 14.04</strong></p>
<h2>编写Shell脚本</h2>
<p>首先，我们要编写一个shell脚本，脚本主要执行的逻辑如下：</p>
<p>显示mysqld进程状态，如果判断进程未在运行，那么输出日志到文件，然后启动mysql服务，如果进程在运行，那么不执行任何操作，可以选择性输出监测结果。</p>
<p>可能大家对于shell脚本比较陌生，在这里推荐官方的shell脚本文档来参考一下</p>
<p><a href="http://wiki.ubuntu.org.cn/Shell%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80" data-original-title="" title="">Ubuntu Shell 编程基础</a></p>
<p>shell脚本的后缀为sh，在任何位置新建一个脚本文件，我选择在 /etc/mysql 目录下新建一个 listen.sh 文件。</p>
<p>执行如下命令：</p>
'''
	deal = Tool()
	print deal.test(a)
