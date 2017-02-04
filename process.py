# encoding=utf-8

import time
import multiprocessing
from random import random
import requests
from requests.exceptions import ConnectionError
'''
def process(num):
	time.sleep(num)
	print 'Process:', num

if __name__ == '__main__':
	for i in range(5):
		p = multiprocessing.Process(target=process, args=(i,))
		p.start()

	print 'CPU number:' + str(multiprocessing.cpu_count())
	for p in multiprocessing.active_children():
		print 'Child process name:' + p.name + ' id: ' + str(p.pid)

	print 'Process Ended'
'''

class MyProcess(multiprocessing.Process):
	"""docstring for MyProcess"""
	def __init__(self, loop, lock):
		multiprocessing.Process.__init__(self)
		self.loop = loop
		self.lock = lock

	def run(self):
		for count in range(self.loop):
			time.sleep(0.1)
			self.lock.acquire()
			print 'Pid: ' + str(self.pid) + ' LoopCount: ' + str(count)
			self.lock.release()

#############################
###Semaphore#######
buffer1 = multiprocessing.Queue(10)
empty = multiprocessing.Semaphore(2)
full = multiprocessing.Semaphore(0)
lock = multiprocessing.Lock()

class Consumer(multiprocessing.Process):
	"""docstring for Consumer"""
	def __init__(self, pipe):
		multiprocessing.Process.__init__(self)
		self.pipe = pipe

	def run(self):
		self.pipe.send('Consumer Words')
		print 'Consumer Received:', self.pipe.recv()
		'''global buffer1, empty, full, lock
		while True:
			full.acquire()
			lock.acquire()
			#print 'Consumer pop an element'
			print 'Consumer get ', buffer1.get() 
			time.sleep(1)
			lock.release()
			empty.release()'''

class Producer(multiprocessing.Process):
	"""docstring for Producer"""
	def __init__(self, pipe):
		multiprocessing.Process.__init__(self)
		self.pipe = pipe

	def run(self):
		print 'Producer Received:', self.pipe.recv()
		self.pipe.send('Producer Words')
		'''global buffer1, empty, full, lock
		while True:
			empty.acquire()
			lock.acquire()
			num = random()
			#print 'Producer append an element'
			print 'Producer put ', num
			buffer1.put(num)
			time.sleep(1)
			lock.release()
			full.release()'''
'''			
def function(index):
	print 'Start process: ', index
	time.sleep(3)
	print 'End process', index

if __name__ == '__main__':
	pool = multiprocessing.Pool(processes=3)
	for i in xrange(4):
		result = pool.apply_async(function, (i,)) #pool.apply(function, (i,)) #apply_async为非阻塞式的，apply为阻塞式的
		print result.get()

	print 'Started processes'
	pool.close()
	pool.join()
	print 'Subprocess done.'
'''
def scrape(url):
	try:
		print requests.get(url)
	except ConnectionError:
		print 'Error Occured ', url
	finally:
		print 'URL ', url, ' Scraped'

if __name__ == '__main__':
	pool = multiprocessing.Pool(processes=3)
	urls = [
		'https://www.baidu.com',
		'http://www.meituan.com/',
		'http://blog.csdn.net/',
		'http://dsfalsdjfl.net'
	]
	pool.map(scrape, urls)
'''
if __name__ == '__main__':
	lock = multiprocessing.Lock()
	for i in range(10,15):
		p = MyProcess(i, lock)
		#p.daemon = True #设置为true，当父进程结束后，子进程会自动被禁止
		p.start()
		#p.join() #当所有子进程都执行完毕后，关闭所有

	#print 'Main Process Ended!'
	
	pipe = multiprocessing.Pipe()
	p = Producer(pipe[0])
	c = Consumer(pipe[1])
	p.daemon = c.daemon = True
	p.start()
	c.start()
	p.join()
	c.join()
	print 'Ended!'
	'''

