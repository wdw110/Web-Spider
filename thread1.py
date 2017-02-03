# encoding=utf-8

import time
import thread
import threading
'''
# 为线程定义一个函数
def print_time(threadName, delay):
	count = 0
	while count <= 5:
		time.sleep(delay)
		count += 1
		print "%s: %s" %(threadName, time.ctime(time.time()))

# 创建两个线程
try:
	thread.start_new_thread(print_time, ("Thread-1", 2,))
	thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
	print "Error: unable to start thread"

while 1: #让主程序一直在等待
	pass

print 'Main Finished'
'''
exitFlag = 0

class myTread(threading.Thread):  #继承父类threading.Thread
	"""docstring for myTread"""
	def __init__(self, threadTD, name, counter):
		threading.Thread.__init__(self)
		self.threadTD = threadTD
		self.name = name
		self.counter = counter

	def run(self):   #把要执行的代码写到run函数里面，线程在创建后会直接运行run函数
		print "Starting " + self.name
		# 获得锁，成功获得锁后返回True
		# 可选的timeout参数不填时将一直阻塞直到获得锁定
		# 否则超时后将返回False
		threadLock.acquire()
		print_time(self.name, self.counter, 5)
		# 释放锁
		threadLock.release()
		print "Exiting " + self.name

def print_time(threadName, delay, counter):
	while counter:
		if exitFlag:
			thread.exit()
		time.sleep(delay)
		print "%s: %s" %(threadName, time.ctime(time.time()))
		counter -= 1

threadLock = threading.Lock()
threads = []

#创建新线程
thread1 = myTread(1, "Thread-1", 1)
thread2 = myTread(2, "Thread-2", 2)

#开启线程
thread1.start()
thread2.start()

#添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

#等待所有线程完成
for t in threads:
	t.join()
	
print "Exiting Main Thread"

