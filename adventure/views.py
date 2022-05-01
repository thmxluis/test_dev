
# Django Rest Framework
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView
from rest_framework import mixins, viewsets

# Models and Serializers
from adventure import models, notifiers, repositories, usecases
from adventure.models import validate_number_plate, Vehicle, ServiceArea

# Serializers
from adventure.serializers import (
    VehicleModelSerializer,
    ServiceAreaModelSerializer,
    JourneySerializer)


class GetVehicleAPIView(generics.ListCreateAPIView):
    """ Get vehicles  """

    serializer_class = VehicleModelSerializer

    def get_queryset(self):
        """ Return all vehicles or a vehicle by license plate """

        plate = self.kwargs.get("plate", None)
        if plate:
            if validate_number_plate(plate):
                return Vehicle.objects.filter(number_plate=plate)
            else:
                raise ValidationError("Invalid license plate")

        return Vehicle.objects.all()


class CreateVehicleAPIView(APIView):
    def post(self, request: Request) -> Response:
        payload = request.data
        vehicle_type = models.VehicleType.objects.get(
            name=payload["vehicle_type"])
        vehicle = models.Vehicle.objects.create(
            name=payload["name"],
            passengers=payload["passengers"],
            vehicle_type=vehicle_type,
        )
        return Response(
            {
                "id": vehicle.id,
                "name": vehicle.name,
                "passengers": vehicle.passengers,
                "vehicle_type": vehicle.vehicle_type.name,
            },
            status=201,
        )


class GetServiceAreaAPIView(generics.ListCreateAPIView):
    """ Get service area """

    serializer_class = ServiceAreaModelSerializer

    def get_queryset(self):
        """ Returns all service areas or one service area per kilometer """

        kilometer = self.kwargs.get("kilometer", None)
        if kilometer:
            return ServiceArea.objects.filter(kilometer=kilometer)

        return ServiceArea.objects.all()


class CreateServiceAreaAPIView(APIView):
    def post(self, request: Request) -> Response:
        payload = request.data
        left_station = models.ServiceArea.objects.get(
            pk=payload["left_station"]) if "left_station" in payload else None
        right_station = models.ServiceArea.objects.get(
            pk=payload["right_station"]) if "right_station" in payload else None
        service_area = models.ServiceArea.objects.create(
            kilometer=payload["kilometer"],
            gas_price=payload["gas_price"],
            left_station=left_station,
            right_station=right_station
        )

        return Response(
            {
                "id": service_area.id,
                "kilometer": service_area.kilometer,
                "gas_price": service_area.gas_price,
                "left_station": service_area.left_station,
                "right_station": service_area.right_station
            },
            status=201
        )


class StartJourneyAPIView(generics.CreateAPIView):
    serializer_class = JourneySerializer

    def perform_create(self, serializer) -> None:
        repo = self.get_repository()
        notifier = notifiers.Notifier()
        usecase = usecases.StartJourney(repo, notifier).set_params(
            serializer.validated_data
        )
        try:
            usecase.execute()
        except usecases.StartJourney.CantStart as e:
            raise ValidationError({"detail": str(e)})

    def get_repository(self) -> repositories.JourneyRepository:
        return repositories.JourneyRepository()
