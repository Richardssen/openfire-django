'''
Created on Apr 28, 2015

@author: nishant.nawarkhede
'''
from requests.auth import HTTPBasicAuth
import requests
from testapp import settings
from lxml import etree


class Openfire:
    
    def __init__(self,username,password,server):
        self.username = username
        self.password = password
        self.server = server
        
    def getAllusers(self):
        
        '''
        this function returns all the users which are registered.
        input parameter - None
        output - list of dictionaries
        '''
        
        url = '/plugins/userService/users'
        r=requests.get(self.server+url, auth=HTTPBasicAuth(self.username, self.password))
        root = etree.fromstring(r._content)
        print r._content
        l=[]
        for i in root:
            d={}
            for j in i:
                d[j.tag]= j.text
            l.append(d)
            
        return l
    
    def getCurrentUserInfo(self,username):
        
        '''
        this function returns selected users data such as username , name  and email 
        '''
        
        url = '/plugins/userService/users/'+username
        r=requests.get(self.server+url, auth=HTTPBasicAuth(self.username, self.password))
        root = etree.fromstring(r._content)
        d={}
        for i in root:
            d[i.tag]= i.text 
        l=[]
        l.append(d)
        return l
    
    def updateUser(self,username,name,email):
        
        '''
        this function will update selected user.
        which field can update ? name and email.
        input -> username , email
        
        '''
        
        url = '/plugins/userService/users/'+username
        
        xml='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <user>
            <username>%s</username>
            <name>%s</name>
            <email>%s</email>
            <properties>
                <property key="keyname" value="value"/>
            </properties>
        </user>'''%(username,name,email)
        
        headers = {'Content-Type': 'application/xml'}
        
        r=requests.put(self.server+url,data=xml,headers=headers, auth=HTTPBasicAuth(self.username, self.password))
        
    def createNewUser(self,username,password,name,email):
        '''
        this function will create new user.
        input -> username , password , name and email
        
        '''
        url='/plugins/userService/users'
        xml='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <user>
            <username>%s</username>
            <password>%s</password>
            <name>%s</name>
            <email>%s</email>
        </user>'''%(username,password,name,email)
        headers = {'Content-Type': 'application/xml'}
        r=requests.post(self.server+url,data=xml,headers=headers, auth=(self.username, self.password))
        
    def deleteUser(self,username):
        '''
        this function will delete existing user.
        input -> username
        '''
        url='/plugins/userService/users/'+username
        r=requests.delete(self.server+url, auth=HTTPBasicAuth(self.username, self.password))
        
    def lockUser(self,username):
        '''
        this function will lock the selected user.
        After locked user wil be unable to login.
        input -> username
        '''
        url = '/plugins/userService/lockouts/'+username
        r=requests.post(self.server+url,auth=(self.username, self.password))
        
    def unlockUser(self,username):
        '''
        this function will unlock the selected user.
        After unlocked, user will be unable to login.
        input -> username
        '''
        url = '/plugins/userService/lockouts/'+username
        r=requests.delete(self.server+url,auth=(self.username, self.password))
        
    def viewFriends(self,username):
        '''
        this function will return all the all the friends for user
        '''
        url='/plugins/userService/users/%s/roster'%username
        r=requests.get(self.server+url,auth=(self.username, self.password))
        root = etree.fromstring(r._content)
        l=[]
        for i in root:
            d={}
            for j in i:
                d[j.tag]= j.text
            l.append(d)
        return l
    
    def addNewFriend(self,username,frndname):
        '''
        this function will add new friend to the user
        '''
        
        url='/plugins/userService/users/%s/roster'%username
        xml='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <rosterItem>
            <jid>%s@vspl011</jid>
            <nickname>%s@vspl011</nickname>
            <subscriptionType>3</subscriptionType>
        </rosterItem>'''%(frndname,frndname)
        headers = {'Content-Type': 'application/xml'}
        r=requests.post(self.server+url,data=xml,headers=headers, auth=('admin', 'admin'))
        if r.status_code==201:
            url='/plugins/userService/users/%s/roster'%frndname
            xml='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
            <rosterItem>
            <jid>%s@vspl011</jid>
            <nickname>%s@vspl011</nickname>
            <subscriptionType>3</subscriptionType>
            </rosterItem>'''%(username,username)
            headers = {'Content-Type': 'application/xml'}
            r=requests.post(self.server+url,data=xml,headers=headers, auth=('admin', 'admin'))
        print 'I am testing everything'
        
