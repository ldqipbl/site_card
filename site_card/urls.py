"""site_card URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from mainapp import views

from site_card import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.main),
    path('about_me/', views.about_me, name='about_me'),
    path('career/', views.career, name='career'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('resume/', views.resume, name='resume'),
]

if settings.DEBUG:
    urlpatterns += static(
            settings.MEDIA_URL, 
            document_root=settings.MEDIA_ROOT
    )
