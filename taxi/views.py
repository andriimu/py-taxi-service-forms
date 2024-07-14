from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    DeleteView, 
    ListView, 
    UpdateView, 
    CreateView, 
    DetailView,
)

from .models import (
    Driver, 
    Car, 
    Manufacturer,
)


@login_required
def index(request):
    """View function for the home page of the site."""

    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "num_visits": num_visits + 1,
    }

    return render(request, "taxi/index.html", context=context)

#ManufacturePart
class ManufacturerListView(LoginRequiredMixin, ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    template_name = "taxi/manufacturer_list.html"
    paginate_by = 5

class ManufacturerUpdateView(LoginRequiredMixin, UpdateView):
    model = Manufacturer
    fields = ['name', 'country']
    template_name = 'taxi/manufacturer_form.html'
    success_url = reverse_lazy('taxi:manufacturer-list')

class ManufacturerDeleteView(LoginRequiredMixin, DeleteView):
    model = Manufacturer
    template_name = 'taxi/manufacturer_confirm_delete.html'
    success_url = reverse_lazy('taxi:manufacturer-list') 

class ManufacturerCreateView(LoginRequiredMixin, CreateView):
    model = Manufacturer
    fields = ['name', 'country']
    template_name = 'taxi/manufacturer_form.html'
    success_url = reverse_lazy('taxi:manufacturer-list') 

#CarPart
class CarListView(LoginRequiredMixin, ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.all().select_related("manufacturer")

class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    fields = ['model', 'manufacturer', 'drivers']
    template_name = 'taxi/car_form.html'
    success_url = reverse_lazy('taxi:car-list')

class CarDetailView(LoginRequiredMixin, DetailView):
    model = Car

class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'taxi/car_confirm_delete.html'
    success_url = reverse_lazy('taxi:car-list')

class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['model', 'manufacturer', 'drivers']
    template_name = 'taxi/car_form.html'
    success_url = reverse_lazy('taxi:car-list')

class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    fields = ['model', 'manufacturer', 'drivers']
    template_name = 'taxi/car_form.html'
    success_url = reverse_lazy('taxi:car-list')

#DriverPart
class DriverListView(LoginRequiredMixin, ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(LoginRequiredMixin, DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars__manufacturer")
