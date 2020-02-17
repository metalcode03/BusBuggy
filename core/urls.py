from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    
    path('', views.index_views, name='home'),
    
    path('events/information', views.event_views, name='info'),
    
    path('booking/bus/search/<slug>', views.add_to_bookings, name='addhire'),
    
    path('bus/register', views.bus_hire_view, name='bookbus'),
    
    path('aboutus', views.aboutUs_page, name='about'),
    
    path('faQ', views.faQ_page, name='faQ'),
        
    path('booking/bus/search', views.SearchView.as_view(), name='searchpath'),
    
    path('booking/<int:pk>', views.BookingBusDetail.as_view(), name='bookingdetail'),
    
    path("booking/bus/direction/<int:pk>/<slug>", views.DirectionDetail.as_view(), name="direction_detail"),

    # path('hiring', views.hirebus, name='hiringbus'),

    # path('booking', booking_views, name='book'),
    
    # path(
        
    #     "informaa1276765433niaganalanajanaanaianau34aranaeanawana324apanaoana456543akanqanyana56banatanhanaban45456774",

    #     name='booked'
    
    # )
    
]
