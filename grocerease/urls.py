"""grocerease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import include
from app import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('grocerease/create_list', app_views.CreateList.as_view(), name='create_list'),
    path('grocerease/add_list_item/<int:pk>/', app_views.AddListItem.as_view(), name='add_list_item'),
    path('grocerease/delete_list_item/<int:pk>/', app_views.UpdateListItem.as_view(), name='delete_list_item'),
    path('grocerease/edit_list_item/<int:pk>/', app_views.UpdateListItem.as_view(), name='edit_list_item'),
    path('grocerease/delete_list/<int:pk>/', app_views.DeleteList.as_view(), name='delete_list' ),
    path('grocerease/register', app_views.Register.as_view(), name='register'),
]
