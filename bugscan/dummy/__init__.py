#!/usr/bin/env python
# -*- coding: utf-8 -*-
Bugscan = 'https://www.bugscan.net/'
import six
if six.PY3:
    import imp
    import os
    DIR, _ = os.path.split(__file__)
    common = imp.load_compiled("common", os.path.join(DIR, "common3.pyc"))
    from common import *

else:
    from common2 import *
    import common2 as common

import util
import DNS
import threadpool
from functools import partial
from fingerprint import FingerPrint
from dnslog import DNSLog

import hackhttp
import hackhttp as hh
hackhttp = hh.hackhttp()

fingerprint = FingerPrint()

_G = {
    'scanport': False,
    'subdomain': False,
    'target': 'www.abc.com',
    'disallow_ip': ['127.0.0.1'],
    'kv': {},
    'udomain': "test",
    # 'user_dict':'http://192.168.0.158/1.txt'
    # 'pass_dict':'http://192.168.0.158/1.txt'
    "custom_dict":{}
}


util._G = _G

dnslog = DNSLog()


def information(*args):
    print(args)


def debug(fmt, *args):
    print(fmt % args)


LEVEL_NOTE = 0
LEVEL_INFO = 1
LEVEL_WARNING = 2
LEVEL_HOLE = 3


def _problem(level, body, uuid=None, log=[]):
    debug('[LOG] <%s> %s (uuid=%s)', ['note', 'info',
                                      'warning', 'hole'][level], body, str(uuid))
    if log:
        if isinstance(log, dict):
            log = [log]
        for l in log:
            print(l['response']["header"])


security_note = partial(_problem, LEVEL_NOTE)
security_info = partial(_problem, LEVEL_INFO)
security_warning = partial(_problem, LEVEL_WARNING)
security_hole = partial(_problem, LEVEL_HOLE)


def task_push(service, arg, uuid=None, target=None):
    if uuid is None:
        uuid = str(arg)

    debug('[JOB] <%s> %s (%s/%s)', service, arg, uuid, target)
