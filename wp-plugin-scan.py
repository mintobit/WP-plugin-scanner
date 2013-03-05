#!/usr/bin/env python

import argparse
import sys
import re
import urllib

argParser = argparse.ArgumentParser()
argParser.add_argument('-s', '--scan', metavar='<website url>', dest='url', help='scan website at <website url>')
argParser.add_argument('-u', '--update', type=int, metavar='<page number>', dest='pageN', help='update the list of plugins from wordpress.org up to <page number>')
args = argParser.parse_args()

def _argumentsNumber():
	return len(sys.argv) - 1

def _isUrl(url):
	pattern = re.compile('^https?://[\w\d\-\.]+/(([\w\d\-]+/)+)?$')
	if pattern.match(url):
		return True
	else:
		return False

def _isWebsiteAlive(url):
	try:
		if urllib.urlopen(url).getcode() == 200:
			print url + ' is alive...'
		else:
			print url + ' seems to be down...'
	except IOError as e:
		print e

def scan(url):
	try:
		plugins = open('plugins.txt')
		for line in plugins.read().split('\n'):
			if line:
				code = urllib.urlopen(url + 'wp-content/plugins/' + line + '/').getcode()
				if code != 404:
					print line + '[+]'
	except IOError as e:
		print e