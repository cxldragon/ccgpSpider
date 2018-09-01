# -*- coding: utf-8 -*-

#+++++++++++++++++++++++++++++++++++++++++++++
#Created By CxlDragon 2018.8.30
#json配置文件类，调用方法
#+++++++++++++++++++++++++++++++++++++++++++++

###  data_dict = {"a":"1", "b":"2"}
##   JsonConf.set(data_dict)
##   即可在当前目录下生成json文件：config.json

import json 
import os
class JsonConf:
    '''json配置文件类'''
    @staticmethod
    def store(data):
        with open("config.json", 'w') as json_file:
            json_file.write(json.dumps(data, indent=4))
    @staticmethod  
    def load():
        if not os.path.exists('config.json'):
            with open("config.json", 'w') as json_file:
                pass       
        with open('config.json') as json_file:
            try:
                data = json.load(json_file)
            except:
                #print('读取json文件失败')
                data = {}
            return data
        
    @staticmethod
    def save(data_dict):
        json_obj = JsonConf.load()
        for key in data_dict:
            json_obj[key] = data_dict[key]
        JsonConf.store(json_obj)
        #print(json.dumps(json_obj, indent=4))

#用于测试
if __name__=="__main__":
    data =  {
        "mail_info":
        {
        "from": "xxxx@xxx.cn",
        "to": "xxxx@xxx.cn",
        "hostname": "smtp.xxx.cn",
        "username": "xxxx@xxx.cn",
        "password": "xxxx",
        "mail_subject": "",
        "mail_text": "",
        "mail_encoding": "utf-8",
        "mail_att":""}
        }
    JsonConf.save(data)
    
