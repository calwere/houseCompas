from django.urls import path
from .views import home,HouseList,HouseDetail,MoverList,MoverDetails,AgentList,IndexList,ContactCreateView, map_view, HouseListAPIView,FacilitiesListAPIView

urlpatterns = [
    path('', IndexList.as_view(), name='home'),
    path('properties/', HouseList.as_view(),name='houses'),
    path('property/<int:pk>/', HouseDetail.as_view(),name='house'),

    path('movers/',MoverList.as_view(),name='movers'),
    
    path('movers/<int:pk>/',MoverDetails.as_view(),name='mover'),

    path('agents/',AgentList.as_view(),name="agent"),

    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('map/', map_view, name='map_view'),
    path('api/houses/', HouseListAPIView.as_view(), name='house-list'),
    path('api/facilities/', FacilitiesListAPIView.as_view(), name='facility-list')

]
