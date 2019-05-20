"""insta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
 
from django.contrib import admin
from django.urls import include, path
from images import views
from django.conf.urls.static import static

  #include function allows to reference another URLconf
 
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('images.urls')),

    #url for registration
    path('accounts/', include('registration.backends.simple.urls')),

]