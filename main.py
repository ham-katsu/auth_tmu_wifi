# -*- coding: utf-8 -*-
import urllib.parse
import urllib.request
import time
url = 'http://1.1.1.1:10080/cgi-bin/adeflogin.cgi'
auth_data = {'name' : 'yourID(u~~~~~~~)', 'pass' : 'your password' }
d = urllib.parse.urlencode(auth_data)
d = d.encode('Shift-JIS')
header = {"Request URI":"/cgi-bin/adeflogin.cgi"}
req = urllib.request.Request(url,d,header,method = "POST")
print('ready')
while(True):
    res = urllib.request.urlopen(req)
    print(res.getcode())
    time.sleep(10)

