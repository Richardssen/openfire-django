# Create your views here.
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from openfireapp.pyopenfire import Openfire
from openfireapp.forms import EditUser,CreateNewUser,AddFriend

SERVER_URL='http://nishant-vaio:9090'
ADMIN_USER_NAME='admin'
ADMIN_PASSWORD='nishant'
def index(request):
    o=Openfire(ADMIN_USER_NAME,ADMIN_PASSWORD,SERVER_URL)
    all_users =  o.getAllusers()
    return render_to_response('index.html',{'all_users':all_users})

def edituser(request,username):
    o=Openfire(ADMIN_USER_NAME,ADMIN_PASSWORD,SERVER_URL)
    if request.method=="GET":
        existing_data = o.getCurrentUserInfo(username)
        form=EditUser(initial={'username': existing_data[0].get('username'),'name':existing_data[0].get('name'),'email':existing_data[0].get('email')})
    else:
        form = EditUser(request.POST)
        if form.is_valid():
            name  = form.cleaned_data['name']
            email  = form.cleaned_data['email']
            o.updateUser(username,name,email)
            return HttpResponseRedirect('/')
    
    return render(request, 'edituser.html', {
        'form': form,'username':username
    })
    
def createNewUser(request):
    if request.method=="GET":
        form=CreateNewUser()
    else:
        form = CreateNewUser(request.POST)
        if form.is_valid():
            username  = form.cleaned_data['username']
            password  = form.cleaned_data['password']
            name  = form.cleaned_data['name']
            email  = form.cleaned_data['email']
            o=Openfire(ADMIN_USER_NAME,ADMIN_PASSWORD,SERVER_URL)
            o.createNewUser(username, password,name,email)
        
    return render(request, 'createNewUser.html', {'form': form
    })
    
def deleteUser(request,username):
    o=Openfire(ADMIN_USER_NAME,ADMIN_PASSWORD,SERVER_URL)
    o.deleteUser(username)
    return HttpResponseRedirect('/')

def lockUser(request,username):
    o=Openfire(ADMIN_USER_NAME,ADMIN_PASSWORD,SERVER_URL)
    o.lockUser(username)
    return HttpResponseRedirect('/')

def unlockUser(request,username):
    o=Openfire(ADMIN_USER_NAME,ADMIN_PASSWORD,SERVER_URL)
    o.unlockUser(username)
    return HttpResponseRedirect('/')

def viewfriends(request,username):
    o=Openfire(ADMIN_USER_NAME,ADMIN_PASSWORD,SERVER_URL)
    data=o.viewFriends(username)
    all_users=o.getAllusers()
    
    if request.method=="GET":
        form=AddFriend(initial={'username':username})
    else:
        form = AddFriend(request.POST)
        if form.is_valid():
            username  = form.cleaned_data['username']
            friendname = form.cleaned_data['friendname']
            o=Openfire(ADMIN_USER_NAME,ADMIN_PASSWORD,SERVER_URL)
            o.addNewFriend(username, friendname)
            
    return render(request, 'viewfriends.html', {'data': data,'form':form,'username':username
    })
    