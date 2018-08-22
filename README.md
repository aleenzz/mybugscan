# mybugscan
fofa_api+bugscan插件扫描
# 用途
主要用于找靶机地址，也可以用于批量测试
#结构
```
│  1.txt
│  run.py
│  
└─bugscan
    │  exp.py
    │  exp.pyc
    │  __init__.py
    │  __init__.pyc
    │  
    └─dummy
            common2.pyc
            common3.pyc
            __init__.py
            __init__.pyc
```
# 设置

1.请把exp放在bugscan目录下

2.exp请设置timeout超时,否则扫描到死ip会很慢 eg:code, head, res, errcode, log= hackhttp.http(target,timeout=3)

3.请设置run.py的fofa_api

# 测试截图
 ![image](https://github.com/aleenzz/mybugscan/raw/master/1.png)
 
# 免责申明
程序仅供研究交流,用于非法与本人无关
