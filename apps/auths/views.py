from django.shortcuts import render, redirect
from django import template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from django.core.exceptions import PermissionDenied
from django.template import loader
from django.urls import reverse
from django.contrib.auth.models import User
import random
from django.contrib.auth.hashers import make_password, check_password


# @login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    # html_template = loader.get_template('home/index.html')
    html_template = loader.get_template('auths/login.html')
    return HttpResponse(html_template.render(context, request))




def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    elif not request.user.is_authenticated:
        context = {'user': 'IBA'}

        if request.method == "POST":
            result = {

            }
            return JsonResponse(result)
        else:

            html_template = loader.get_template('auths/login.html')
            return HttpResponse(html_template.render(context, request))




def subadmin_login(request):
    context = {'user': 'Subadmin'}

    if request.method == "POST":
        result = {

        }
        return JsonResponse(result)
    else:

        html_template = loader.get_template('auths/login.html')
        return HttpResponse(html_template.render(context, request))






def admin_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('../../../backend/admin/dashboard/')
    elif not request.user.is_authenticated:
        context = {'user': 'Admin'}

        if request.method == "POST":
            data = json.loads(request.body)
            print(data)

            raw_username = data["username"]
            raw_password = data["password"]

            admin = authenticate(request, username=raw_username, password=raw_password)
            print("It has passed")
            print(admin)

            if admin is not None:
                auth_login(request, admin)
                print("He has logged in...")

                result = {
                    "boolean_val": True,
                    "status": "success",
                    "user": "Admin",
                    # "session_id": request.session['username']
                }

                return JsonResponse(result)
            
        else:
            print(context)
            html_template = loader.get_template('auths/login.html')
            return HttpResponse(html_template.render(context, request))


# def logout_view(request):
#     logout(request)

#     html_template = loader.get_template('auths/login.html')
#     return HttpResponse(html_template.render(context, request))




def register(request):
    context = {'segment': 'index'}

    if request.method == "POST":
        result = {

        }
        return JsonResponse(result)
    else:
        
        html_template = loader.get_template('auths/register.html')
        return HttpResponse(html_template.render(context, request))





def error_403(request, exception):
    return render(request,'errors/page-403.html')

def error_404(request, exception):
    return render(request,'errors/page-404.html')

def error_500(request, exception):
    return render(request,'errors/page-500.html')



def set_password(self, raw_password):
    algo = 'sha1'
    salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
    hsh = get_hexdigest(algo, salt, raw_password)
    self.password = '%s$%s$%s' % (algo, salt, hsh)
    return self.password






































# @login_required(login_url="/login/")
# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:

#         load_template = request.path.split('/')[-1]
#         print(load_template)

#         if load_template == 'admin':
#             return HttpResponseRedirect(reverse('admin:index'))
#         context['segment'] = load_template

#         html_template = loader.get_template('home/' + load_template)
#         return HttpResponse(html_template.render(context, request))

#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template('errors/page-404.html')
#         return HttpResponse(html_template.render(context, request))

#     except:
#         html_template = loader.get_template('errors/page-500.html')
#         return HttpResponse(html_template.render(context, request))




# from .forms import LoginForm, SignUpForm


# Create your views here.


# def login_view(request):
#     form = LoginForm(request.POST or None)

#     msg = None

#     if request.method == "POST":

#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect("/")
#             else:
#                 msg = 'Invalid credentials'
#         else:
#             msg = 'Error validating the form'

#     return render(request, "auths/login.html", {"form": form, "msg": msg})


# def register_user(request):
#     msg = None
#     success = False

#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get("username")
#             raw_password = form.cleaned_data.get("password1")
#             user = authenticate(username=username, password=raw_password)

#             msg = 'User created - please <a href="/login">login</a>.'
#             success = True

#             # return redirect("/login/")

#         else:
#             msg = 'Form is not valid'
#     else:
#         form = SignUpForm()

#     return render(request, "auths/register.html", {"form": form, "msg": msg, "success": success})






