from .models import Flight, Reservation, Passenger
from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view


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


@api_view(['POST'])
def find_flights(request):
    """
    This function will return the flights searched by user
    """
    flights = Flight.objects.filter(
        departureCity=request.data['departureCity'], arrivalCity=request.data['arrivalCity'], dateOfDeparture=request.data['dateOfDeparture'])
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def save_reservation(request):
    # retrieving the flight from database
    flight = Flight.objects.get(id=request.data['id'])

    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.lastName = request.data['lastName']
    passenger.middleName = request.data['middleName']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger

    reservation.save()

    return Response(status=status.HTTP_201_CREATED)
