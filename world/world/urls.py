"""world URL Configuration

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
from django.contrib import admin
from django.urls import path
from town.views import register, user_login, user_logout, user_udpate, profile_user
from people import views
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Content.as_view(), name='index'),
    path('user_login/', user_login, name='user_login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('tovar/<slug>/', views.TovarInfo.as_view(), name='tovar_info'),
    path('update_user/<slug>/', user_udpate, name='update_user'),
    path('profile_user/', profile_user, name='profile_user'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
