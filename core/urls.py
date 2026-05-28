from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    
    # یہ لائن لازمی ہونی چاہیے
    path('marketplace/', views.marketplace, name='marketplace'),
    
    path('robots.txt', lambda r: HttpResponse("User-agent: *\nAllow: /", content_type="text/plain")),
]