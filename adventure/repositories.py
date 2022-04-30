from django.utils import timezone

from adventure import models


class JourneyRepository:
    def get_or_create_car(self) -> models.VehicleType:
        car, _ = models.VehicleType.objects.get_or_create(name="car", max_capacity=5)
        return car

    def create_vehicle(
        self, name: str, passengers: int, vehicle_type: models.VehicleType
    ) -> models.Vehicle:
        return models.Vehicle.objects.create(
            name=name, passengers=passengers, vehicle_type=vehicle_type
        )

    def create_journey(self, vehicle: models.Vehicle) -> models.Journey:
        return models.Journey.objects.create(
            vehicle=vehicle, start=timezone.now().date()
        )
