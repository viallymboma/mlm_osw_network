from django.urls import path, re_path
from apps.user_accounts import views

urlpatterns = [
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/profile/', views.admin_profile, name='admin_profile'),

    path('subadmin/dashboard/', views.subadmin_dashboard, name='subadmin_dashboard'),
    path('subadmin/profile/', views.subadmin_profile, name='subadmin_profile'),

    path('iba/dashboard/', views.iba_dashboard, name='iba_dashboard'),
    path('iba/profile/', views.iba_profile, name='iba_profile'),

    path('', views.logout_view, name="logout"),

    path('tree/graphical_tree_view/', views.graphical_tree_view, name='graphical_tree_view'),
]





# http://127.0.0.1:8000/backend/admin/dashboard/