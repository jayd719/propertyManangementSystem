"""
URL configuration for SEVERJSP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from T01homepage.views import homepage
from T01homepage import views as T01
from T02Dashboard import views as T02
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='homepage'),
    path('login/', T01.Login.as_view(redirect_authenticated_user=True), name='loginPage'),
    path('signUser/', T01.Login.as_view(), name='signIn'),
    path('resident_dashbord',T02.dashhome,name='homepage-residents'),
    path('clicked/',T02.clicked,name='clicked')
]
