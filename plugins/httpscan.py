#!/usr/bin/python
# -*- coding: utf-8 -*-
# 多端口请求http
# 支持多线程 
# python httpscan.py example.com timeout  (referer-url)
__author__ = 'kttzd'

import sys
import httplib2
import futures
import time
import hashlib

headers={}
headers['User-Agent']="Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6"

ADDRESS=sys.argv[1]
TIMES=int(sys.argv[2])

#ports=map(str,range(start,stop)
#try:
#    headers['Referer']=sys.argv[5]
#except:
#    pass
HISTORY=[] #历史记录
class test():

    def shell():   #打开文件的时候
        f=open("shell.txt","r")
        shellcode=f.readlines()
        f.close()
        return shellcode
    def history_shell():  #打开写入的文件
        f=open("history.txt","r")
        history_shell=f.readlines()
        f.close()
        return history_shell
#对比打开的记录和历史记录
    def 



#保存记录写入history.txt
    def fwrite():




#打开一个不存在的网页 记录下状态码     ps:也可打开一个不存在的网页记录下read()的长度，和其他对比
def 




class httpscan():
    def __init__(self,ADDRESS,TIMES):
        self.address=ADDRESS
        #self.headers=headers
        self.times=TIMES
    def scan(self,path):
        path=path.replace("\n","")
        h=httplib2.Http(timeout=self.times)
        host="http://"+self.address+path
        HISTORY.append(path)  #保存记录
        #f=open("history.txt","w")
        #print host
        try:
            res,con=h.request(host,"HEAD")
            print host+"---------I GET IT"
        except Exception,e:
            #print e
            pass
        
def main():
    test=httpscan(ADDRESS,TIMES)
    #start = time.time()
    try:
        with futures.ThreadPoolExecutor(max_workers=20) as executor:
            tasks =dict((executor.submit(test.scan,path),path) for path in shell)
            futures.as_completed(tasks)
    except KeyboardInterrupt:
        print "Scan done\n"  #需要修改一下
    finally:
        print "Have a nice day"

if __name__=="__main__":
    main()