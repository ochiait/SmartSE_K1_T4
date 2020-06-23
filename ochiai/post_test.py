#! /usr/bin/python3
# -*- coding: utf-8 -*-
import smbus
from time import sleep

bus=smbus.SMBus(1)
address_gpy2=0x40
register_gpyu=0x5E
register_gpys=0x5F

def read_gpy2():
	data=0
	for i in range(1,11):
	 #11-4bit data
		ue=bus.read_word_data(address_gpy2,register_gpyu)
	 #3-0bit data
		shita=bus.read_word_data(address_gpy2,register_gpys)
		ue=ue & 0xff
		shita=shita & 0xff
		kobetu =((ue*16+shita)/16)/4
		data =data+kobetu
		sleep(0.005)
	average=data/10
	return average
while True:
	inputValue = read_gpy2()
	print(inputValue)
	sleep(1)
"""
＜上記の実行結果＞
Python 3.7.3 (/usr/bin/python3)
>>> %Run post_test.py
48.4640625
52.603125
63.984375
63.984375
17.1078125
15.8140625
11.3734375
7.696875
"""