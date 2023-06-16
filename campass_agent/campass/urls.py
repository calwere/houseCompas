from django.urls import path
from .views import home,HouseList,HouseDetail,MoverList

urlpatterns = [
    path('', home, name='home'),
    path('properties/', HouseList.as_view(),name='houses'),
    path('property/<int:pk>/', HouseDetail.as_view(),name='house'),

    path('movers/',MoverList.as_view(),name='movers'),
]