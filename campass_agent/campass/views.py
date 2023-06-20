from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
# Create your views here.
from .models import Agent , House,Amenities,Mover,Facilities,Contact

from geopy.geocoders import GoogleV3

# geolocator = GoogleV3(api_key='AIzaSyCXEZty_KxWEvPpTx7X00dg4wgPYBhfyrY')

import socket

hostname = socket.gethostname()

ip_address = socket.gethostbyname(hostname)


import ssl
ssl._create_default_https_context = ssl._create_unverified_context





class AgentList(ListView):
    model = Agent
    template_name='agents.html'
    context_object_name = 'agents'








class IndexList(ListView):
    model = Agent
    template_name='index.html'
    context_object_name = 'agents'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the current agent object

        houses = House.objects.all()

        context['houses'] = houses

        return context

   



class AgentDetail(DetailView):
    model = Agent
    context_object_name = 'agent'




class HouseList(ListView):
    model = House
    paginate_by = 6
    context_object_name = 'houses'
    template_name='property.html'



class HouseDetail(DetailView):
    model = House
    context_object_name = 'house'
    template_name='property-single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the current agent object
        house = self.get_object()

        latitude = self.object.latitude
        longitude = self.object.longitude
        
        # Perform reverse geocoding
        geolocator = Nominatim(user_agent="campass_agent_app",timeout=5)
        location = geolocator.reverse(f"{latitude}, {longitude}")

        point1 = f"{latitude}, {longitude}"

     
        
        # Add the location to the context
       

        # Query AnotherModel where agent_id is equal to the current agent ID
        amenities = Amenities.objects.filter(house_id=house.id)

        facilities = Facilities.objects.all()

        movers = Mover.objects.all()

        my_location = geolocator.geocode("Nairobi, Kenya")

        print(my_location)

        lat = my_location.latitude
        lon = my_location.longitude

        my_point = f"{lat}, {lon}"

        for f in facilities:
            point2 = f"{f.latitude}, {f.longitude}"

    
       

       

        distance = geodesic(point1, point2).kilometers
        # Add the queried objects to the context

        distance_mover = geodesic(point1, my_point).kilometers

        context['facilities'] = facilities

        context['movers'] = movers

        context['location'] = location

        context['distance'] = distance
        context['distance_mover'] = distance_mover
        context['amenities'] = amenities

        return context


class MoverList(ListView):
    model = Mover
    paginate_by = 6
    context_object_name = 'movers'
    template_name='movers.html'



class MoverDetails(DetailView):
    model = Mover
    context_object_name = 'mover'
    template_name='movers-single.html'








def home(request):
    return render(request,'index.html')


