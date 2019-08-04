from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user/check/(?P<objects>\d{1,10})',views.data_display,name='data_display'),
    path('logout/',views.index,name="index"),
    path('user/check/done/',views.entry_form_data,name='entry_form_data'),
    path('user/done/',views.entry_form_data,name='entry_form_data'),
    path('user/', views.entry_form,name='entry_form'),
    path('signup/done/login_done/', views.entry_login_data , name='entry_login_data'),
    path('login/login_done/', views.entry_login_data , name='entry_login_data'),
    path('signup/done/', views.entry_signup_data , name='entry_signup_data'),
    path('signup/', views.signup_form , name='signup_form'),
    path('login/' , views.login_form , name='login_form'),
    path('',views.index,name='index')
]