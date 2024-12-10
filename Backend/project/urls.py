"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products', AllProduct.as_view(), name='Productlist'),
    path('api/category', AllCategory.as_view(), name='Categorylist'),
    path('api/createcategory', createCategory.as_view(), name='createCategory'),
    path('api/updatedeletecategory/<int:pk>/', updatedeleteCategory.as_view(), name='updatedeleteCategory'),
    path('api/createproduct', createProduct.as_view(), name='createProduct'),
    path('api/updatedeleteproduct/<int:pk>/', updatedeleteProduct.as_view(), name='updatedeleteProduct'),

]
