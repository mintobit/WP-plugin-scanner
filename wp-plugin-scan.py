#!/usr/bin/env python

import argparse
import sys
import re
import urllib
import lxml.html
import os

def _main():
	argParser = argparse.ArgumentParser()
	argParser.add_argument('-s', '--scan', metavar='<website url>', dest='url', help='scan website at <website url>')
	argParser.add_argument('-u', '--update', type=int, metavar='<page number>', dest='pageN', help='update the list of plugins from wordpress.org up to <page number>')
	args = argParser.parse_args()
	
	if args.url == args.pageN == None:
		argParser.print_help()
	elif args.url != None:
		scan(args.url)
	else:
		update(args.pageN)

def _isUrl(url):
	pattern = re.compile('^https?://[\w\d\-\.]+/(([\w\d\-]+/)+)?$')
	if pattern.match(url):
		return True
	else:
		return False

def _isWebsiteAlive(url):
	try:
		if urllib.urlopen(url).getcode() == 200:
			return True
		else:
			return False
	except IOError as e:
		print e

def _parseHrefs(html):
	doc = lxml.html.document_fromstring(html)
	pattern = re.compile('/plugins/([\w\d\-]+)/')
	pluginsList = []
	links = doc.cssselect('div.plugin-block h3 a')
	for link in links:
		plugin = pattern.search(link.get('href')).group(1)
		pluginsList.append(plugin)
		print plugin + '[+]'
	return pluginsList

def _writePlugins(pluginsList):
	currentDir = os.path.dirname(os.path.realpath(__file__)) + os.path.sep
	pluginsFile = open(currentDir + 'plugins.txt', 'w')
	pluginsFile.write('\n'.join(pluginsList))
	pluginsFile.close()

def scan(url):
	if _isUrl(url) != True:
		print 'The url you entered should match this pattern ^https?://[\w\d\-\.]+/(([\w\d\-]+/)+)?$'
		return
	elif _isWebsiteAlive(url) != True:
		return
	print 'Scanning...'
	currentDir = os.path.dirname(os.path.realpath(__file__)) + os.path.sep
	try:
		pluginsFile = open(currentDir + 'plugins.txt', 'r')
		for line in pluginsFile.read().split('\n'):
			if line:
				code = urllib.urlopen(url + 'wp-content/plugins/' + line + '/').getcode()
				if code != 404:
					print line + '[+]'
	except IOError as e:
		print e

def update(pageN):
	pluginsList = []
	if pageN == 1:
		html = urllib.urlopen('http://wordpress.org/extend/plugins/browse/popular/').read()
		pluginsList = _parseHrefs(html)
	elif pageN == 2:
		html = urllib.urlopen('http://wordpress.org/extend/plugins/browse/popular/').read()
		pluginsList = _parseHrefs(html)
		html = urllib.urlopen('http://wordpress.org/extend/plugins/browse/popular/page/2/').read()
		pluginsList = pluginsList + _parseHrefs(html)
	else:
		for page in range(2, pageN):
			html = urllib.urlopen('http://wordpress.org/extend/plugins/browse/popular/page/' + str(pageN) + '/').read()
			pluginsList = pluginsList + _parseHrefs(html)
	_writePlugins(pluginsList)

if __name__ == "__main__": _main()