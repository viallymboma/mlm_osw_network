from django.urls import path, re_path
from apps.auths import views

urlpatterns = [

    # The home page
    path('', views.login, name='login'),
    path('management/backend/subadmin/', views.subadmin_login, name='login_subadmin'),
    path('management/backend/admin/', views.admin_login, name='login_admin'),
    # path('bad-request-400', views.error_400, name='error_400'),
    path('forbidden-403/', views.error_403, name='error_403'),
    path('not-found-404/', views.error_404, name='error_404'),
    path('server-error-500/', views.error_500, name='server_error_500'),
    path('signup/', views.register, name='register'),
    # path('back/', views.register, name='register'),
    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]

# http://127.0.0.1:8000/management/backend/admin/