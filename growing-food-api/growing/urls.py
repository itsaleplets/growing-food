"""growing URL Configuration

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
from django.urls import path, include, re_path
from rest_framework import routers
from food.views import (
    VegetableView,
    VegetableTypesView,
    VegetablesView,
    VegetableTypeView,
)


router = routers.DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("vegetables/", VegetablesView.as_view({"get": "list"})),
    path("vegetables-type/", VegetableTypesView.as_view({"get": "list"})),
    path("vegetable/", VegetableView.as_view()),
    re_path(r"vegetable/(?P<pk>.+)", VegetableView.as_view()),
    path("vegetable-type/", VegetableTypeView.as_view()),
    re_path(r"vegetable-type/(?P<pk>.+)", VegetableTypeView.as_view()),
]
