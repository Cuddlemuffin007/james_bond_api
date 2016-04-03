from django.db import models


class Vehicle(models.Model):
    make = models.CharField(max_length=20)
    vehicle_model = models.CharField(max_length=20)

    def __str__(self):
        return '{} {}'.format(self.make, self.vehicle_model)


class Character(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    alias = models.CharField(max_length=50, null=True, blank=True)
    ally = models.BooleanField(default=False)
    villain = models.BooleanField(default=False)
    henchman = models.BooleanField(default=False)
    bond_girl = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Gadget(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    owner = models.ForeignKey(Character, null=True)

    def __str__(self):
        return self.name


class BondActor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    bond_actor = models.ForeignKey(BondActor, null=True)
    characters = models.ManyToManyField(Character, blank=True)
    vehicles = models.ManyToManyField(Vehicle, blank=True)
    gadgets_weapons = models.ManyToManyField(Gadget, blank=True)

    def __str__(self):
        return self.title
