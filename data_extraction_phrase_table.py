#!/usr/bin/python

# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import sys

file_name=sys.argv[1]
data=open(file_name,'r')
for line in data:
    req_data=line.split('|||')
    hindi_phrase=req_data[1]
    hindi_phrase=hindi_phrase.strip()
    hindi_phrase=hindi_phrase.decode('UTF-8')
    print hindi_phrase.encode('UTF-8')
