from django.shortcuts import render
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


# Weather Views 
import urllib.request
import json


 # import viewsets
from rest_framework import viewsets
 
# import local data
from .serializers import ImageSerializer
from .models import Image
 
# create a viewset For Image
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


# Login form 

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



def home(request):
    
    import requests
    import json
  
    news_api_requests=requests.get(" https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=60dc141986e64bec9611c24ade739e31  ")
    api = json.loads(news_api_requests.content)
    return render(request,'home.html',{'api':api})


def index(request):
    import requests
    import json
  
    news_api_requests=requests.get("https://newsapi.org/v2/everything?q=bitcoin&apiKey=60dc141986e64bec9611c24ade739e31  ")
    api = json.loads(news_api_requests.content)

    return render(request,'index.html',{'api':api})


def App(request):
    import requests
    import json
  
    news_api_requests=requests.get(" https://newsapi.org/v2/everything?q=apple&from=2023-07-20&to=2023-07-20&sortBy=popularity&apiKey=60dc141986e64bec9611c24ade739e31  ")
    api = json.loads(news_api_requests.content)

    return render(request,'App.html',{'api':api})


def New(request):
    import requests
    import json
  
    news_api_requests=requests.get(" https://newsapi.org/v2/top-headlines?q=trump&apiKey=60dc141986e64bec9611c24ade739e31 ")
    api = json.loads(news_api_requests.content)

    return render(request,'New.html',{'api':api})


# Video 
def video(request):
    return render(request,'video.html')


def a(request):
    return render(request,'a.html')

def b(request):
    return render(request,'b.html')

# Payment 

def khalthi(request):
     img = Image.objects.all()
     return render(request,'khalthi.html',{'img':img})

def epay(request):
     img = Image.objects.all()
     return render(request,'epay.html',{'img':img})



# Create your views here.
def gmail(request):

    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        send_mail(subject, message, settings.EMAIL_HOST_USER,
                  [email], fail_silently=False)
        return render(request, 'email_sent.html', {'email': email})

    return render(request, 'gmail.html', {})


def All(request):
    # Post Form Submit
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        concern=request.POST['concern']
        print(name,email,phone,concern)
        obj=Contact(name=name,email=email,phone=phone,concern=concern)
        obj.save() 
        return HttpResponse("<h1>Cograulation for Submited the Form.</h1>") 
    #For image api
    img = Image.objects.all()
    return render(request,'All.html',{'img':img})
    
    
    
    
    # Login form


@login_required(login_url='login')
def AllPage(request):
    return render (request,'All.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')


        if not uname or not email or not pass1 or not pass2:
          #  return HttpResponse ("<h1 >Please fill up all the  fields.</h1>")
         return redirect('fail') 


        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('All')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

  
 
# Sign Up Form Fill Up .
def fail(request):
    return render(request,'fail.html')
  
  
  
# Weather Views 
  
def weather(request):

    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=073cb99cb2f4c57e5aae6c2cfd7d0162').read()
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "weather.html", data)
