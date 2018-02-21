#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import json
import urllib
import urllib3
import sys
import time
def ilmtApi(first, last, text):
    pool = urllib3.PoolManager()
    url = 'http://api.ilmt.iiit.ac.in/hin/pan/%s/%s' % (first, last)
    method = 'POST'
    headers = {'Content-Type':'application/x-www-form-urlencoded', 'charset':'UTF-8'}
    data = pool.urlopen(method, url, headers = headers, body = text).data
    return json.loads(data)
def check_float(word_encoded):
    try:
        if float(word_encoded):
            return True
    except ValueError:
        return False

def get_phrases(sentence):
    try:
        tillChunker = ilmtApi('1', '5', "input=%s" % (sentence))
        payload = "input=" + urllib.quote(tillChunker['chunker-5'].encode('UTF-8'))
        print payload
        wx2utf = ilmtApi('14', '14', payload)["wx2utf-14"]
        text= wx2utf.split()
        check=0
        phrase_set=[]
        phrase=""
        for word in text:
            word_encoded=word.encode('UTF-8')
            if check_float(word_encoded):
                if check==int(float(word_encoded)):
                    phrase=phrase+text[text.index(word_encoded)+1].strip()+" "
                else:
                    check=int(float(word_encoded))
                    if phrase!="":
                        phrase_set.append(phrase)
                    phrase=""
        return phrase_set
    except:
        return -1
    #return phrase_set

def main():
    final_phrase_set=[]
    file_name=sys.argv[1]
    data=open(file_name,'r')
    f=open('count.txt','w')
    count=0;
    for line in data:
        count+=1
        f.write(str(count)+'\n')
        phrase_set=get_phrases(line)
        if phrase_set==-1:
            time.sleep(10)
            phrase_set=get_phrases(line)
        for i in phrase_set:
            print i.encode('UTF-8')

    """
    for i in final_phrase_set:
        print i.encode('UTF-8')
    """
main()
