#!/usr/bin/python
import cgi, cgitb
import redis
import os
import json
print "Content-type:text/html\n\n"
cgitb.enable()

class RedisDataApi:

    def __init__(self):
        self.r = self.REDIS_Connect()
        pass

    def REDIS_Connect(self):
        try:
            r =  redis.Redis(host="localhost" ,port=6379, password="", decode_responses=True,db=2)
        except Exception as e:
            print e
        return r
    
    def read_data_from_file(self):
        #f = open('/var/www/html/Test_Case_Output/5131_final_result.txt')
        f = open('/var/www/html/Test_Case_Output/SYMSPELL_GERMAN_v1.txt')
        data_dict = [line.strip('\n').split('\t') for line in f.readlines()]
        map_dict = {}
        header = data_dict[0]
        for line in data_dict[1:]:
            #value = dict(zip(header,line))
            key = line[0]
            #key = '%s'%(line[2],line[5])
            if not map_dict.get(key,[]): map_dict[key] = {}
            map_dict[key][line[1]] = '%s_%s'%(line[2],line[3])
        
        with self.r.pipeline() as pipe:
            for h_id, hat in map_dict.items():
                pipe.hmset(h_id, hat)
            pipe.execute()

    def serch_in_redis(self,text):
        serTEXT = self.r.hgetall(text)
        if not serTEXT: return '' 
        serTEXT = map(lambda x:(x[0],x[1].split('_')),serTEXT.items())
        serTEXT = dict(serTEXT)
        
        return serTEXT

    def collect_values(self):
        form = cgi.FieldStorage()
        text = form.getvalue('serText')
        if text:
            return text
        else:
            return ""

    def run(self):
        text = self.collect_values()
        #text = "aud"
        print json.dumps(self.serch_in_redis(text))

if __name__ == "__main__":
    
    obj = RedisDataApi()
    obj.run()
