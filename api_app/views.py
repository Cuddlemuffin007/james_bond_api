from rest_framework.generics import ListAPIView, RetrieveAPIView
from api_app.models import Movie, Character, Vehicle, Gadget, BondActor
from api_app.serializers import MovieSerializer, CharacterSerializer, \
                                VehicleSerializer, GadgetSerializer, \
                                BondActorSerializer


class MovieListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CharacterListAPIView(ListAPIView):
    serializer_class = CharacterSerializer

    def get_queryset(self):
        if self.kwargs.get('char_type') == 'allies':
            return Character.objects.filter(ally=True)
        elif self.kwargs.get('char_type') == 'villains':
            return Character.objects.filter(villain=True)
        elif self.kwargs.get('char_type') == 'henchmen':
            return Character.objects.filter(henchman=True)
        elif self.kwargs.get('char_type') == 'bond-girls':
            return Character.objects.filter(bond_girl=True)
        else:
            return Character.objects.all()


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


class CharacterByTypeRetrieveAPIView(RetrieveAPIView):
    serializer_class = CharacterSerializer

    def get_queryset(self):
        if self.kwargs.get('char_type') == 'allies':
            return Character.objects.filter(ally=True)
        elif self.kwargs.get('char_type') == 'villains':
            return Character.objects.filter(villain=True)
        elif self.kwargs.get('char_type') == 'henchmen':
            return Character.objects.filter(henchman=True)
        elif self.kwargs.get('char_type') == 'bond-girls':
            return Character.objects.filter(bond_girl=True)
        else:
            return Character.objects.all()


class VehicleRetrieveAPIView(RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class GadgetRetrieveAPIView(RetrieveAPIView):
    queryset = Gadget.objects.all()
    serializer_class = GadgetSerializer


class BondActorRetrieveAPIView(RetrieveAPIView):
    queryset = BondActor.objects.all()
    serializer_class = BondActorSerializer
