from .models import Flight, Reservation, Passenger
from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets

# Create your views here.


class FlightViewSet(viewsets.ModelViewSet):
    """
    This class will add all crud based operations both primary key based
    and non-primary key based
    """
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
