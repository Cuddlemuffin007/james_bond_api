from rest_framework import serializers
from api_app.models import Movie, Character, Vehicle, Gadget, BondActor


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        depth = 1


class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle


class GadgetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gadget
        depth = 1


class BondActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = BondActor
