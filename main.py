# -*- coding: utf-8 -*-
import urllib.parse
import urllib.request
import time
url = 'http://1.1.1.1/cgi-bin/adeflogin.cgi:10080'
auth_data = {'name' : 'yourid', 'pass' : 'yourpass' }
d = urllib.parse.urlencode(auth_data)
d = d.encode('utf-8')

httpshandler = urllib.request.HTTPSHandler()
pro = urllib.request.ProxyHandler({})
opener = urllib.request.build_opener(pro,httpshandler)
urllib.request.install_opener(opener)

req = urllib.request.Request(url,d,method = "POST")
print('ready')
req.add_header("User-Agent","Mozilla/5.0 (Macintosh) AppleWebkit() Chrome/47.0.2526.106")
while(True):
    res = urllib.request.urlopen(req)
    print(res.getcode())
    time.sleep(10)

