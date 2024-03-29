"""mytestsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from views import hello, add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload_image/',include('upload_image.urls')),
    re_path(r'hello/([A-Za-z]+)/', hello),
    re_path(r'([0-9]+)/plus/([0-9]+)/', add),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)