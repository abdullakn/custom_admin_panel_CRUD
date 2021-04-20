from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.views.generic import View
from .models import *
from myapp.forms import *
from django.contrib.sessions.models import Session
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from myapp.filter import UserFilter
# Create your views here.


class Registration(View):
    def get(self, request):
        return render(request, 'registration.html', {})


    def post(self,request):
        data = request.POST
        name = data['username']
        email = data['email']
        pwd = data['password']
        phnnumber=data['phone']
        place=data['place']


        if MyUserData.objects.filter(username=name).exists():
            return render(request,'registration.html',{'error':"username not available"})
        else:    
            


            r1 = MyUserData.objects.create_user(username=name,email=email, password=pwd,phone=phnnumber,place=place)
            r1.save()
        # user=authenticate(request,username=name,password=pwd)
        # if user is not None:
        #     login(request,user)
        return redirect('/login')


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/home')
        return render(request, 'login.html', {})
    
    def post(self,request):
        data=request.POST
        us=data["username"]
        psw=data["password"]
        if(us=="admin"):
            return render(request,'login.html',{"error":"**admin cannot login this way"})
        else:    
            user=authenticate(request,username=us,password=psw)
            print(user)
            if user is not None:
                login(request,user)
                return render(request,'home.html',{'name':user})

                # return redirect('/home')
            else:
                return render(request,'login.html',{"error":"**Invalid user Name or Password"})
    

@login_required(login_url="/login")
def Home(request):
     user=request.user
     print(user)
     return render(request, 'home.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Logout(request):
        logout(request)
        request.session['is_value'] = True
        return redirect('/login')





@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminlogin(request):

    if request.session.has_key('is_value'):
        return redirect('newadmin')
    
    if request.method == "POST":
        username="admin"
        password="12345"
        data=request.POST
        user=data['username']
        pswd=data['password']

        if(username == user and password == pswd):
            request.session['is_value']=True
            return redirect('newadmin')
        else:
            return render(request,'adminlogin.html',{'error':"**Invalid username or password"})    
    else:        
        return render(request,'adminlogin.html')    



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def newadmin(request):
   
    user=MyUserData.objects.exclude(is_staff=1)
    if  request.session.has_key('is_value'):
        # if request.method == "POST":
        #     search=request.POST['search']
        #     user=MyUserData.objects.filter(username=search)
        #     return render(request,'adminnew.html',{'users':user}) 
        user_filter=UserFilter(request.GET,queryset=user)
  
        return render(request,'adminnew.html',{'users':user_filter})  
       
    else:
        return redirect('adminlogin')    



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminlogout(request):
    
    del request.session['is_value']
    return redirect('adminlogin')    

       
        
     
      



def custom_admin(request):
    user=MyUserData.objects.all()
    return render(request,'admin.html',{'users':user})    


def update(request,id):
    data=MyUserData.objects.get(id=id)
    print(data
    )
    if request.method == "POST":
        newdata=request.POST
        
        email=newdata['email']
        phone=newdata['phone']
        place=newdata['place']
        
        data.email=email
        data.phone=phone
        data.place=place
        data.save()
        return redirect('/newadmin/')

    else:
        if request.session.has_key('is_value'):
            return render(request,'update.html',{'data':data})
        else:
            return redirect('adminlogin')  
     

    
  

    # return render(request,'update.html',{'data':data})


def delete(request,id):
    MyUserData.objects.get(id=id).delete()
    return redirect('newadmin')    



def adduser(request):

    if request.method == "POST":
        data=request.POST
        username=data['username']
        email=data['email']
        phone=data['phone']
        place=data['place']
        password=data['password']
        if MyUserData.objects.filter(username=username).exists():
            return render(request,'adduser.html',{'error':"username already taken"})
        else:
            r1 = MyUserData(username=username,email=email, password=password,phone=phone,place=place)
            r1.save()
            return redirect('/newadmin')

    else:
        if request.session.has_key('is_value'):
            return render(request,'adduser.html')  
        else:
            return redirect('adminlogin')  


            
    # return render(request,'adduser.html')    

    # if request.method == "GET":
    #     if request.session.has_key('is_logged'): 
    #         return redirect('adduser')   
    #     else:
    #         return redirect('adminlogin')  



   

    

