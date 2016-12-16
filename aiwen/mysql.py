#encoding=utf-8

import time
import MySQLdb

class Mysql(object):
	"""docstring for Mysql"""

	def getCurrentTime(self):
		return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

	def __init__(self, arg):
		try:
			self.db = MySQLdb.connect('127.0.0.1','root','','test')
			self.cur = self.db.cursor()
		except MySQLdb.Error, e:
			print self.getCurrentTime(),'连接数据库错误，原因%d：%s' %(e.args[0],e.args[1])

	#插入数据
	def insertData(self,table,my_dict):
		try:
			self.db.set_character_set('utf8')
			cols = ', '.join(my_dict.keys())
			values = '"," '.join(my_dict.values())
			sql = 'insert into %s (%s) values (%s)' %(table,cols,'"'+values+'"')
			try:
				result = self.cur.execute(sql)
				insert_id = self.db.insert_id()
				self.db.commit()
				#判断是否执行成功
				if result:
					return insert_id
				else:
					return 0
			except MySQLdb.Error,e:
				#发生错误时回滚
				self.db.rollback()
				#主键唯一，无法插入
				if "key 'PRIMARY'" in e.args[1]:
					print self.getCurrentTime(),'数据已存在，未插入数据'
				else:
					print self.getCurrentTime(),'插入数据失败，原因%d：%s' %(e.args[0],e.args[1])
		except MySQLdb.Error,e:
			print self.getCurrentTime(),'数据库错误，原因%d：%s' %(e.args[0],e.args[1])