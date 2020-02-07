from itertools import chain

from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from accounts.models import User
from location_app.models import Location, Directions

from .models import (
    
    BookingBus,
    
    EventType
    
    )



    
# this is the homepage
# @login_required
def index_views(request):
    
    # user = User.objects.get(username=request.user)
    
    booked_b = Directions.objects.all()[:3]
    
    context = {
        
        'book_b': booked_b,
        
    }
    return render(request, 'home_templates/index.html', context)





# this is the bus search and book pages
class SearchView(ListView):
    
    template_name = 'home_templates/searchpage.html'
    
    paginate_by = 20
    
    count = 0
    
    # for getting context_data
    def get_context_data(self, *args, **kwargs):
        
        context = super().get_context_data(*args, **kwargs)
        
        context['count'] = self.count or 0
        
        context['query'] = self.request.GET.get('q')
        
        return context
    
    # for getting queryset
    def get_queryset(self):
        
        request = self.request
        
        query = request.GET.get('q', None)
        
        if query is not None:
            
            direction_results = Directions.objects.search(query)
            
            queryset_chain = chain(
                
                direction_results,
                
            )
            qs = sorted(
                
                queryset_chain,
                
                key=lambda instance: instance.pk,
                
                reverse=True
            )
            
            self.count = len(qs)
            
            return qs
        
        return Directions.objects.none()



# this is for viewing events
@login_required
def event_views(request):
    
    user = User.objects.get(username=request.user)
    
    # booked_b = BookingB.objects.all()
    
    hire_b = HiringBus.objects.filter(user=user)
    
    context = {
        # 'book_b': booked_b,
        'hire_b': hire_b
    }
    return render(request, 'home_templates/booked.html', context)




def bus_hire_view(request):
    bus_directions = Directions.objects.all()[:8]
    
    context = {
        
        'bus_directions':bus_directions
        
    }
    return render(request, 'home_templates/bookbus.html', context)



#used to book for bus 
@login_required
def add_to_bookings(request, slug):
    directions = get_object_or_404(Directions, slug=slug)

    hire_qs = BookingBus.objects.filter(
        
        user=request.user,
        
        direction=directions,
        
        hired=True
        
    )

    if hire_qs.exists():
        
        messages.info(request, 'this booking already exist')
        
        return redirect('/home', slug=slug)
    
    else:
        
        hire_bus, created = HiringBus.objects.get_or_create(
            
            user=request.user,
            
            direction=directions,
            
            hired=True
            
        )[:2]
        
        hire_bus.save()
        
        messages.info(
            
            request,
            
            'Your Booking was Successful, Feel Free to book another'
            
        )  
    return redirect('/home', slug=slug)


    
    
    # hire_qs = Hiring.objects.filter(user=request.user, hired=True)
    # if hire_qs.exists():
    #     hire = hire_qs[0]
    #     #check if the hiring bus is in the hire
    #     if hire.direction.filter(direction__slug=directions.slug).exists():
    #         hire_bus
        


# Create your views here.
# @login_required
# def booking_views(request):
    # if request.method == 'POST':
    #     book_form = BookingBForm(request.POST)
    #     if book_form.is_valid():
    #         your_locations = book_form.cleaned_data.get('your_location')
    #         destinations = book_form.cleaned_data.get('destination')
    #         users = User.objects.get(username=request.user)
    #         book_saver = HiringB.objects.create(
    #             user=request.user,
    #             your_location=your_locations,
    #             destination=destinations
    #         )
    #         book_saver.save()
    #         # book_form.instance = request.user
    #         # book_form.save()
    #         return redirect('/events/information')
    # else:
    #     book_form = BookingBForm()
    # context = {
    #     'book_form':book_form
    # }
    # return render(request, 'about.html', context)
    # return render(request, 'home_templates/booking.html', context)





def aboutUs_page(request):
    
    return render(request, 'order/about.html')

def faQ_page(request):
    
    return render(request, 'order/faQ.html')

class BookingBusDetail(DetailView):
    
    model = BookingBus
    
    template_name='applications/properties-single.html'

class DirectionDetail(DetailView):
    
    model = Directions
    
    template_name = 'applications/direction-single.html'