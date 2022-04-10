from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import json
from django.template import loader

# Create your views here.

# @login_required
def admin_dashboard(request):
    
    if request.user.is_authenticated:
        if request.method == "POST":
            # data = json.loads(request.body)
            # print(data)
            result = {
                "boolean_val": True,
                "user": "Admin",
                "page": "Admin Dashboard"
            }
            return JsonResponse(result)
        else:
            segment = {
                "components-notifications": True,
                "components": True,
                "components-": True,
                "components-forms": True,
                "components-modals": True,
                "components-typography": True,
                "tables-bootstrap-": True,
                "settings": True,
                "transactions": True,
                "dashboard": True,
                "settings": True,
            }
            html_template = loader.get_template('accounts/dashboard.html')
            return HttpResponse(html_template.render(segment, request))
            # return render(request, 'accounts/dashboard.html')
    elif not request.user.is_authenticated:
        segment = {
            "boolean_false": "False",
            "user": "Admin",
            "msg": "Please Login before you can access Back Office"
        }
        # return HttpResponseRedirect('../../../management/backend/admin/')
        html_template = loader.get_template('auths/login.html')
        return HttpResponse(html_template.render(segment, request))


def graphical_tree_view(request):

    # We are gonna pull data in two different ways
    # first one is by selecting a user or IBA and serializing him
    # then pulling the 2 (left and right) users who hava him as 
    # sponsor. and in turn also pulling data of those 2 left and 
    # right users. this i gonna give us an object that we can 
    # easily pass to json response to our javascript on the UI
    # the second way we can get the data is by using an incremental
    # Number for each users this number will pull data and organize it
    # as object and send it via json and javascript will do BFS on it
    # and plot a tree with that data.
    
    if request.user.is_authenticated:
        if request.method == "POST":
            # data = json.loads(request.body)
            # print(data)
            result = {
                "boolean_val": True,
                "user": "Admin",
                "page": "Admin Dashboard"
            }
            return JsonResponse(result)
        else:
            segment = {
                "components-notifications": True,
                "components": True,
                "components-": True,
                "components-forms": True,
                "components-modals": True,
                "components-typography": True,
                "tables-bootstrap-": True,
                "settings": True,
                "transactions": True,
                "dashboard": True,
                "settings": True,
            }

            html_template = loader.get_template('accounts/graphical_tree_display.html')
            return HttpResponse(html_template.render(segment, request))
            # return render(request, 'accounts/dashboard.html')
    elif not request.user.is_authenticated:
        segment = {
            "boolean_false": "False",
            "user": "Admin",
            "msg": "Please Login before you can access Back Office"
        }

        # return HttpResponseRedirect('../../../management/backend/admin/')
        html_template = loader.get_template('auths/login.html')
        return HttpResponse(html_template.render(segment, request))



# @login_required
def admin_profile(request):
    if request.user.is_authenticated:
        
        if request.method == "POST":
            result = {
                "boolean_val": True,
                "user": "Admin",
                "page": "Admin Profile Page"
            }
            return JsonResponse(result)
        else:
            context = {
                "boolean_admin": True,
                "user": "Admin",
                "page": "Admin Profile Page"
            }
            html_template = loader.get_template('accounts/profile.html')
            return HttpResponse(html_template.render(context, request))
            # return render(request, 'accounts/dashboard.html')
        
    elif not request.user.is_authenticated:
        segment = {
            "boolean_false": "False",
            "user": "Admin",
            "msg": "Please Login before you can access Back Office"
        }
        # return HttpResponseRedirect('../../../management/backend/admin/')
        html_template = loader.get_template('auths/login.html')
        return HttpResponse(html_template.render(segment, request))





@login_required
def subadmin_dashboard(request):
    if request.method == "POST":
        result = {
            "boolean_val": True,
            "user": "Subadmin",
            "page": "Subadmin Dashboard"
        }
        return JsonResponse(result)
    else:
        html_template = loader.get_template('accounts/dashboard.html')
        return HttpResponse(html_template.render(context, request))
        # return render(request, 'accounts/dashboard.html')

@login_required
def subadmin_profile(request):
    if request.method == "POST":
        result = {
            "boolean_val": True,
            "user": "Subadmin",
            "page": "Subadmin Profile Page"
        }
        return JsonResponse(result)
    else:
        html_template = loader.get_template('accounts/profile.html')
        return HttpResponse(html_template.render(context, request))
        # return render(request, 'accounts/dashboard.html')





@login_required
def iba_dashboard(request):
    if request.method == "POST":
        result = {
            "boolean_val": True,
            "user": "IBA",
            "page": "IBA Dashboard"
        }
        return JsonResponse(result)
    else:

        html_template = loader.get_template('accounts/dasboard.html')
        return HttpResponse(html_template.render(context, request))
        # return render(request, 'accounts/settings.html')

@login_required
def iba_profile(request):
    if request.method == "POST":
        result = {
            "boolean_val": True,
            "user": "IBA",
            "page": "IBA Profile Page"
        }
        return JsonResponse(result)
    else:

        html_template = loader.get_template('accounts/profile.html')
        return HttpResponse(html_template.render(context, request))
        # return render(request, 'accounts/dashboard.html')





@login_required
def logout_view(request):
    logout(request)
    context = {
        "logout_message": "You are Logout! See you soon!"
    }
    return HttpResponseRedirect('../management/backend/admin/')
    # html_template = loader.get_template('accounts/login.html')
    # return HttpResponse(html_template.render(context, request))






