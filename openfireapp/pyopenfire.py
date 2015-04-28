'''
Created on Apr 28, 2015

@author: nishant.nawarkhede
'''
from requests.auth import HTTPBasicAuth
import requests
from testapp import settings

class Openfire:
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
    def getAllusers(self):
        r=requests.get('http://vspl011:9090/plugins/userService/users', auth=HTTPBasicAuth('admin', 'admin'))
        return r._content
    

o=Openfire(settings.ADMIN_USERNAME,settings.ADMIN_PASSWORD)
print o.getAllusers()