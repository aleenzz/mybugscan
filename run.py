#!/usr/bin/python
# -*- coding: utf-8 -*-
from  bugscan import *
import fofa
import argparse
import importlib

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--search','-s',help="your fofa grammar ")
    parser.add_argument('--payloda','-p',help='your payloda')
    args = parser.parse_args()
    exps = importlib.import_module('bugscan.%s'% args.payloda)
    # 你自己的fofa api
    email, key = ('xxx@qq.com','xxxx')
    client = fofa.Client(email, key)
    query_str = u"%s" % args.search
    urls = []
    # 从第1页查到第2页
    for page in range(1,2):
        # 查询F币剩余数量
        fcoin = client.get_userinfo()["fcoin"]
        print "Fb:%s" %fcoin
        if fcoin < 92:
            break
        data = client.get_data(query_str,page=page,fields="ip,port")
        for ip,port in data["results"]:
            if port == "443":
                urls.append('https://%s'% ip)
            else:
                urls.append('http://%s:%s'%(ip,port))
        for url in urls:
        	try:
        		print url
        		exps.audit("%s/"%url)
        	except:
        		print "sorry:%s"%url
if __name__ == "__main__":
    main()