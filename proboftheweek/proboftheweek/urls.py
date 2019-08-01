"""
Definition of urls for proboftheweek.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
#from app import forms, views
from proboftheweek import views


urlpatterns = [
    
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('weekly/', views.weekly, name='weekly'),
    path('submit/', views.submit_ans, name='submit'),
    path('archive/', views.ArchiveView.as_view(), name='archive'),
    path('archive/<int:question_id>/', views.arch_q, name='archive_q'),
    path('success/', views.success, name='success'),
    path('answer/', views.answer, name='answer'),
    path('responses/', views.QListView.as_view(), name='responses'),
    path('responses/<int:question_id>/', views.ResponsesView.as_view(), name='responses_q'),
    #path('contact/', views.contact, name='contact'),
    #path('about/', views.about, name='about'),
    #path('login/',
    #     LoginView.as_view
    #     (
    #         template_name='app/login.html',
    #         authentication_form=forms.BootstrapAuthenticationForm,
    #         extra_context=
    #         {
    #             'title': 'Log in',
    #             'year' : datetime.now().year,
    #         }
    #     ),
    #     name='login'),
    #path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    
]
