#!/usr/bin/env python

import urllib.request
import sys
import os
import threading
import platform

def replace_hosts(systemtype='Window'):
    try:
        if systemtype == 'Windows':
            os.system('copy %SystemRoot%\System32\drivers\etc\hosts  %SystemRoot%\System32\drivers\etc\hosts_bak')
            os.system('copy hosts %SystemRoot%\System32\drivers\etc\hosts')
            os.system('ipconfig /flushdns')
            print ('It\'s done on Windows! And Try your browser!')
        elif systemtype == "Linux":
            os.system('cp /etc/hosts /etc/hosts_bak')
            os.system('mv ./hosts /etc/hosts')
            os.system('sudo /etc/init.d/networking restart ')
            print ('It\'s done on Linux! And Try your browser!')
    except Exception as e:
        print (e)

def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    global url
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    downsize=blocknum * blocksize
    if downsize >= totalsize:
    	downsize=totalsize
    s ="%.2f%%"%(percent)+"====>"+"%.2f"%(downsize/1024/1024)+"M/"+"%.2f"%(totalsize/1024/1024)+"M \n"
    sys.stdout.write(s)
    sys.stdout.flush()
    if percent == 100:
        print('下载完成,正在备份替换您设备上的hosts文件,请等待......')
        replace_hosts(platform.system())
        print('更新hosts文件完成.OK!')
        input('输入任意键继续...')

def downimg():
    print('#####################################')
    print('QQ:3036512853')
    print('#####################################')
    print('正在请求hosts Server,请等待......')
    url='https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
    filename=os.path.basename(url)
    urllib.request.urlretrieve(url, filename, callbackfunc)
	
'''
启动线程下载
'''
threading.Thread(target=downimg,args=('')).start()


