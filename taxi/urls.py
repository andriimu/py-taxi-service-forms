from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
    CarCreateView,
    CarUpdateView,
    CarDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    #Manufactures
    path("manufacturers/", ManufacturerListView.as_view(),  name="manufacturer-list",),
    path('manufacturer/create/', ManufacturerCreateView.as_view(), name='manufacturer-create'),
    path('manufacturer/<int:pk>/update/', ManufacturerUpdateView.as_view(), name='manufacturer-update'),
    path('manufacturer/<int:pk>/delete/', ManufacturerDeleteView.as_view(), name='manufacturer-delete'),
    #Cars
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path('car/create/', CarCreateView.as_view(), name='car-create'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car-update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),
    #Drivers
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
