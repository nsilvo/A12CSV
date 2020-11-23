#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from bs4.element import Comment
import requests

#url = "http://admit1.ssvc.com:8585/?f=schedule"

#xml_data = requests.get(url).content
infile = open("filmschedule.xml","r")
xml_data = infile.read()

soup = BeautifulSoup(xml_data, "lxml")

events = soup.find_all("event")
name = events.find_all("name")
for i in range(0, len(name)):
    print (name[i].get_text())
