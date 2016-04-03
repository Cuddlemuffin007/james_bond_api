from rest_framework.generics import ListAPIView, RetrieveAPIView
from api_app.models import Movie, Character, Vehicle, Gadget, BondActor
from api_app.serializers import MovieSerializer, CharacterSerializer, \
                                VehicleSerializer, GadgetSerializer, \
                                BondActorSerializer


class MovieListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CharacterListAPIView(ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class AllyListAPIView(CharacterListAPIView):

    def get_queryset(self):
        return Character.objects.filter(ally=True)


class BondGirlListAPIView(CharacterListAPIView):

    def get_queryset(self):
        return Character.objects.filter(bond_girl=True)


class VillainListAPIView(CharacterListAPIView):

    def get_queryset(self):
        return Character.objects.filter(villain=True)


class HenchmanListAPIView(CharacterListAPIView):

    def get_queryset(self):
        return Character.objects.filter(henchman=True)


class VehicleListAPIView(ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class GadgetListAPIView(ListAPIView):
    queryset = Gadget.objects.all()
    serializer_class = GadgetSerializer


class BondActorListAPIView(ListAPIView):
    queryset = BondActor.objects.all()
    serializer_class = BondActorSerializer


class MovieRetrieveAPIView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CharacterRetrieveAPIView(RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class VehicleRetrieveAPIView(RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class GadgetRetrieveAPIView(RetrieveAPIView):
    queryset = Gadget.objects.all()
    serializer_class = GadgetSerializer


class BondActorRetrieveAPIView(RetrieveAPIView):
    queryset = BondActor.objects.all()
    serializer_class = BondActorSerializer
