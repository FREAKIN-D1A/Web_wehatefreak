from django.shortcuts import render, HttpResponse, redirect
# from .forms import UserRegForm, UserLoginForm
from django.contrib.auth import login , logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post

# Create your views here.

def index_view(request):
    context = {
        "title": "We Hate Freak"
    }
    return render(request, "blog/index.html", context)


def registration_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password1"]
        confirm_password = request.POST["password2"]
        if password == confirm_password :
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                login(request,user)
                return redirect('blog:homepage_view',username=user.username)
            except:
                context = {"error": "The username is taken ,try again please"}
                return render(request, "blog/registration.html", context)
            
        else:
            context = {"error": "The passwords do not match. Try again"}
            return render(request, "blog/registration.html", context)
    else:
        context ={
            "title": "Registration",
        }
        return render(request, "blog/registration.html", context)



def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog:homepage_view',username=user.username)
        else:
            return HttpResponse("not good.Wrong username or password. try again babe")


    else:
        context ={
            "title": "Login",
        }
        return render(request, "blog/login.html", context)


@login_required(login_url='/login')
def homepage_view(request, username):
    if request.method == "POST":
        content = request.POST["content"]
        user =  User.objects.get(username=username)
        new_post = user.post_set.create(content=content, date_posted=timezone.now(), time_posted=timezone.now() )
        return redirect("blog:homepage_view", username=user.username)
    else:
        posts = Post.objects.order_by('-time_posted').order_by('-date_posted')
        context = {
            "title":"Home",
            "posts":posts,
        }

        return render(request, "blog/home.html", context)


@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    context = {
        "title": "We Hate Freak",
        "logout": "You have been logged out",
        }
    return redirect('blog:index_view',)
   





    