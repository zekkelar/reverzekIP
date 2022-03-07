import socket, os, sys
import requests
import threading
from multiprocessing.dummy import Pool
import os,sys,time
os.path.exists('Sites')
import re
from colorama import Fore								
from colorama import Style								
from colorama import init	
def ip(i):
	i = i.strip()
	i = i.replace("http://", "")
	i = i.replace("https://", "")
	i = i.replace("/", "")
	i = i.replace("\n", "")
	data = socket.gethostbyname(i)
	ok.append(data)
def runip():
	ThreadPool = Pool(500)
	Threads = ThreadPool.map(ip, ooo)

if __name__ == "__main__":
	ooo = input('list : ')
	ooo = open(ooo,'r')
	reks1 = input('save : ')
	ok = []
	print('Please Wait...')
	
	try:
		runip()
	except:
		pass

	ok = set(ok)
	ok = list(ok)
	for hh in ok:
		print ('[$$$]  '+hh)
		with open(reks1,'a') as it:
			it.writelines(hh+'\n')
