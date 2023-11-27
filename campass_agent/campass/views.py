from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
# Create your views here.
from .models import Agent , House,Amenities,Mover,Facilities,Contact
from .forms import ContactForm
from geopy.geocoders import GoogleV3
from django.contrib.gis.db import models

from rest_framework import generics
from .serializers import HouseSerializer, FacilitiesSerializer

# views.py for serializers


class HouseListAPIView(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class FacilitiesListAPIView(generics.ListAPIView):
    queryset = Facilities.objects.all()
    serializer_class = FacilitiesSerializer


from .models import Map

geolocator = GoogleV3(api_key='AIzaSyCXEZty_KxWEvPpTx7X00dg4wgPYBhfyrY')

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
from django.contrib.gis.geos import GEOSGeometry, Point
from django.http import JsonResponse

user_location = None  # Initialize user_location as a global variable
def get_user_location(request):
    if request.method == 'GET':
        # Assuming the latitude and longitude are sent in the request query parameters
        user_latitude = request.GET.get('latitude')
        user_longitude = request.GET.get('longitude')

        if user_latitude and user_longitude:
            # Create a point using the user's provided latitude and longitude
            user_location = Point(float(user_longitude), float(user_latitude), srid=4326)

            # You can perform further operations with the user's location here,
            # such as saving to the database or calculations

            # For this example, let's just return the user's location as a JSON response
            return JsonResponse({'user_location': user_location.geojson})
        else:
            return JsonResponse({'error': 'Latitude and longitude not provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)

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

     
        
# Query AnotherModel where agent_id is equal to the current agent ID
        amenities = Amenities.objects.filter(house_id=house.id)

        facilities = Facilities.objects.all()

        movers = Mover.objects.all()

        # my_location = geolocator.geocode("Nairobi, Kenya")
        # my_location = user_location
        

        # print(my_location)

        # lat = my_location.latitude
        # lon = my_location.longitude

        # my_point = f"{lat}, {lon}"

        for f in facilities:
            point2 = f"{f.latitude}, {f.longitude}"
 
      

        distance = geodesic(point1, point2).kilometers
        print(distance);

#         # Query AnotherModel where agent_id is equal to the current agent ID
#         amenities = Amenities.objects.filter(house_id=house.id)

#         facilities = Facilities.objects.all()

#         movers = Mover.objects.all()

#         my_location = geolocator.geocode("Nairobi, Kenya")

#         print(my_location)

#         lat = my_location.latitude
#         lon = my_location.longitude

#         my_point = f"{lat}, {lon}"

#         for f in facilities:
#             point2 = f"{f.latitude}, {f.longitude}"

    
              

#         distance = geodesic(point1, point2).kilometers
  # Add the queried objects to the context

        distance_mover = geodesic(point1, user_location).kilometers

        context['facilities'] = facilities

        context['movers'] = movers

        context['location'] = location

        context['distance'] = distance
        context['distance_mover'] = distance_mover
        context['amenities'] = amenities

        return context
#         # Add the queried objects to the context

#         distance_mover = geodesic(point1, my_point).kilometers

#         context['facilities'] = facilities

#         context['movers'] = movers

#         context['location'] = location

#         context['distance'] = distance
#         context['distance_mover'] = distance_mover
#         context['amenities'] = amenities

#         return context


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



class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/contact/' 


def map_view(request):
    houses = House.objects.all()
    facilities = Facilities.objects.all()
    return render(request, 'map.html', {'houses': houses, 'facilities': facilities})    
    # return render(request, 'map.html')

def calculate_distance(request):
    # Get user's current location (latitude, longitude)
    user_latitude = request.POST.get('latitude')
    user_longitude = request.POST.get('longitude')

    user_location = Point(float(user_longitude), float(user_latitude))

    # Query all houses and facilities from the database
    houses = House.objects.all()
    facilities = Facilities.objects.all()

    # Calculate distance from user to each house and facility
    house_distances = []
    facilities_distances = []

    for house in houses:
        house_location = Point(house.longitude, house.latitude)
        distance = geodesic(user_location, house_location).kilometers
        house_distances.append({'name': house.name, 'distance': distance})

    for facility in facilities:
        facilities_location = Point(facilities.longitude, facilities.latitude)
        distance = geodesic(user_location, facilities_location).kilometers
        facilities_distances.append({'name': facilities.name, 'distance': distance})

    # Determine the best path (shortest distance)
    shortest_house = min(house_distances, key=lambda x: x['distance'])
    shortest_facility = min(facilities_distances, key=lambda x: x['distance'])

    # Return the best path or distance information
    return render(request, 'distance.html', {
        'user_latitude': user_latitude,
        'user_longitude': user_longitude,
        'shortest_house': shortest_house,
        'shortest_facility': shortest_facility,
    })






      

    
      




