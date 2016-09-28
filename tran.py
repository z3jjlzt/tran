#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#author z3jjlzt.

import requests
import json
import sys

print("########################")
print()
print("        "+sys.argv[1])
print()
r = requests.get("http://fanyi.youdao.com/openapi.do?keyfrom=fangyiguan1&key=500485810&type=data&doctype=json&version=1.1&q="+sys.argv[1])

s = json.loads(r.text)

print(s['translation'][0])
if('basic' in s):
	for txt in s['basic']['explains']:
		print(txt)
elif('web' in s):
	for i in s['web']:
		for j in i['value']:
			print(j)
else:
	print("zzz翻译君未能翻译D-:")
print()
print("########################")

