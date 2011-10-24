#!/usr/bin/env python

import urllib2
import re
import time
import sys

print '+------------------------------------------------------------------------------------------------------+'
print '|			__        ______          _             _                                      |'
print '|			\ \      / /  _ \   _ __ | |_   _  __ _(_)_ __                                 |'
print "|		 	 \ \ /\ / /| |_) | | '_ \| | | | |/ _` | | '_ \                                |"
print '|		  	  \ V  V / |  __/  | |_) | | |_| | (_| | | | | |                               |'
print '|		   	   \_/\_/  |_|     | .__/|_|\__,_|\__, |_|_| |_|                               |'
print '|		                  	   |_|            |___/                                        |'
print '|			       ___  ___ __ _ _ __  _ __   ___ _ __                                     |'
print "|			      / __|/ __/ _` | '_ \| '_ \ / _ \ '__|                                    |"
print '|			      \__ \ (_| (_| | | | | | | |  __/ |                                       |'   
print '|			      |___/\___\__,_|_| |_|_| |_|\___|_|                                       |'
print '|												       |'
print '| @author hookman                                                                                      |'
print '| @email hookman.ru[at]gmail.com                                                                       |'
print '| @version 1.0 											       |'
print '+------------------------------------------------------------------------------------------------------+'
try:
	mode = sys.argv[1]
except IndexError, r:
	mode = ''

try:
	param = sys.argv[2]
except IndexError, r:
	param = ''

p = re.compile('^http://[a-zA-Z0-9\-\.]+/([a-zA-Z0-9\-]+/)?$')
r = re.compile('^[0-9]+$')
if mode == '-scan' and p.match(param):
	url = param
	plugins = open('plugins.txt', 'r')
	print 'Scanning started...'
	for line in plugins.read().split('\n'):
		if line:
			try:
				code = urllib2.urlopen(url + 'wp-content/plugins/' + line + '/').getcode()
				print line + '[+]'
			except urllib2.HTTPError, e:
				continue

elif mode == '-update' and r.match(param):
	pages = int(param) + 1
	plugins = []
	print 'Parsing started...'
	for page in range(1,pages):  
		html = urllib2.urlopen('http://wordpress.org/extend/plugins/browse/popular/page/' + str(page) + '/').read()
		pattern = re.compile('<div class="plugin-block">\n\t<h3><a href="http://wordpress.org/extend/plugins/([a-zA-Z0-9\-]+)/')
		result = pattern.findall(html)
		for res in result:
			plugins.append(res)
			print res + '[+]'
			time.sleep(0.42)

	file = open('plugins.txt', 'w')
	for plugin in plugins:
		file.write(plugin + '\n')
	file.close()
elif mode == '-help':
	print '+------------------------------------------------------------------------------------------------------+'
	print '|   Usage: wp-plugin-scan.py [options]                                                                 |'
	print '|                                                                                                      |'
	print '|   Options:                                                                                           |'
	print '|   -help		show this help message and exit                                                |'
	print '|   -scan URL		scan web site at URL(http://site/ or http://site/wpdir/) for plugins           |'
	print '|   -update INT		parse INT(pages) at wordpress.org for plugins. They are saved at plugins.txt   |'
	print '|												       |'
	print '|   example: ./wp-plugin-scan.py -scan http://wpsite.com/                                              |'
	print '|   example: ./wp-plugin-scan.py -update 989							       |'
	print '+------------------------------------------------------------------------------------------------------+'
else:
	print 'Wrong params!'
