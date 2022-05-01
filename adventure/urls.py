from django.urls import path

from adventure import views
from adventure.views import GetVehicleAPIView, GetServiceAreaAPIView

urlpatterns = [
    path("vehicles/", GetVehicleAPIView.as_view(), name="vehicles"),
    path("vehicles/<str:plate>/", views.GetVehicleAPIView.as_view()),
    path("create-vehicle/", views.CreateVehicleAPIView.as_view()),
    path("service-areas/", views.GetServiceAreaAPIView.as_view()),
    path("service-areas/<int:kilometer>/",
         views.GetServiceAreaAPIView.as_view()),
    path("create-service-area/", views.CreateServiceAreaAPIView.as_view()),
    path("start/", views.StartJourneyAPIView.as_view()),
]
