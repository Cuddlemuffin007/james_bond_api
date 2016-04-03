from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from api_app.models import Vehicle, Character, Gadget, BondActor, Movie
from api_app.serializers import MovieSerializer, CharacterSerializer, VehicleSerializer, \
        GadgetSerializer, BondActorSerializer


class VehicleTestCase(TestCase):

    def setUp(self):
        Vehicle.objects.create(make='Ford', vehicle_model='F-150')
        Vehicle.objects.create(make='Chrysler', vehicle_model='Sebring')

    def test_vehicle_is_displayed_as_make_and_model(self):
        f150 = Vehicle.objects.get(vehicle_model='F-150')
        sebring = Vehicle.objects.get(make='Chrysler')
        self.assertEqual(str(f150), 'Ford F-150')
        self.assertEqual(str(sebring), 'Chrysler Sebring')


class CharacterTestCase(TestCase):

    def setUp(self):
        Character.objects.create(name='Brennon', bio='test test test', ally=True)

    def test_character_is_created_with_required_fields_and_correct_default_values(self):
        me = Character.objects.get(name='Brennon')
        self.assertEqual(me.name, 'Brennon')
        self.assertEqual(me.bio, 'test test test')
        self.assertEqual(me.alias, None)
        self.assertEqual(me.ally, True)
        self.assertEqual(me.henchman, False)
        self.assertEqual(me.villain, False)
        self.assertEqual(me.bond_girl, False)

    def test_can_update_character_object(self):
        me = Character.objects.get(name='Brennon')
        me.ally = False
        me.villain = True
        me.save()
        self.assertEqual(me.ally, False)
        self.assertEqual(me.villain, True)


class GadgetTestCase(TestCase):

    def setUp(self):
        james_bond = Character.objects.create(
                name='James Bond',
                bio='Commander, Royal Navy, MI6 operative',
                alias='007'
                )
        Gadget.objects.create(name='Walther PPK', description='best pistol ever', owner=james_bond)

    def test_gadget_is_created_with_required_fields(self):
        ppk = Gadget.objects.get(name='Walther PPK')
        self.assertEqual(ppk.name, 'Walther PPK')
        self.assertEqual(ppk.description, 'best pistol ever')
        self.assertEqual(ppk.owner, Character.objects.get(alias='007'))


class BondActorTestCase(TestCase):

    def test_bond_actor_has_name(self):
        actor = BondActor.objects.create(name='Idris Elba')
        self.assertEqual(actor.name, 'Idris Elba')


class MovieTestCase(TestCase):

    def setUp(self):
        bond_actor = BondActor.objects.create(name='Idris Elba')
        Movie.objects.create(title='Bond 25', release_date=timezone.now(), bond_actor=bond_actor)

    def test_can_add_many_to_many_rels_to_movie(self):
        movie = Movie.objects.get(title='Bond 25')
        james_bond = Character.objects.create(name='James Bond', alias='007')
        character = Character.objects.create(name='M', bio='head of MI6', ally=True)
        character2 = Character.objects.create(name='Q', bio='head of Q-Branch', alias='Major Boothroyd', ally=True)
        gadget = Gadget.objects.create(name='Omega Seamaster', owner=james_bond)
        vehicle = Vehicle.objects.create(make='Aston Martin', vehicle_model='DB5')

        characters = [james_bond, character, character2]
        for character in characters:
            movie.characters.add(character)
            movie.save()

        movie.gadgets_weapons.add(gadget)
        movie.vehicles.add(vehicle)
        movie.save()

        self.assertEqual(movie.title, 'Bond 25')
        self.assertEqual(movie.bond_actor.name, 'Idris Elba')
        for character in characters:
            self.assertIn(character, movie.characters.all())
        self.assertIn(gadget, movie.gadgets_weapons.all())
        self.assertIn(vehicle, movie.vehicles.all())


class APIViewTestCase(APITestCase):
    client = APIClient()

    def setUp(self):
        Vehicle.objects.create(make='Ford', vehicle_model='F-150')
        Vehicle.objects.create(make='Chrysler', vehicle_model='Sebring')
        bond_actor = BondActor.objects.create(name='Idris Elba')
        movie = Movie.objects.create(title='Bond 25', release_date=timezone.now().date(), bond_actor=bond_actor)
        james_bond = Character.objects.create(name='James Bond', alias='007')
        character = Character.objects.create(name='M', bio='head of MI6', ally=True)
        character2 = Character.objects.create(name='Q', bio='head of Q-Branch', alias='Major Boothroyd', ally=True)
        character3 = Character.objects.create(name='Honey Ryder', ally=True, bond_girl=True)
        character4 = Character.objects.create(name='May Day', henchman=True, bond_girl=True)
        character5 = Character.objects.create(name='Blofeld', villain=True)
        characters = [
                james_bond, character, character2,
                character3, character4, character5
                ]
        gadget = Gadget.objects.create(name='Omega Seamaster', owner=james_bond)
        gadget2 = Gadget.objects.create(name='Walther PPK', description='best pistol ever', owner=james_bond)
        vehicle = Vehicle.objects.create(make='Aston Martin', vehicle_model='DB5')
        for character in characters:
            movie.characters.add(character)
        movie.gadgets_weapons.add(gadget)
        movie.gadgets_weapons.add(gadget2)
        movie.vehicles.add(vehicle)
        movie.save()

    def test_get_movie_list(self):
        url = reverse('movie_list_api_view')
        response = self.client.get(url)
        self.assertEqual(len(response.json()), Movie.objects.count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_character_list(self):
        url = reverse('character_list_api_view')
        response = self.client.get(url)
        self.assertEqual(len(response.json()), Character.objects.count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_ally_list(self):
        url = reverse('ally_list_api_view')
        response = self.client.get(url)
        self.assertEqual(len(response.json()), Character.objects.filter(ally=True).count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_bond_girl_list(self):
        url = reverse('bond_girl_list_api_view')
        response = self.client.get(url)
        self.assertEqual(len(response.json()), Character.objects.filter(bond_girl=True).count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_villain_list(self):
        url = reverse('villain_list_api_view')
        response = self.client.get(url)
        self.assertEqual(len(response.json()), Character.objects.filter(villain=True).count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_henchman_list(self):
        url = reverse('henchman_list_api_view')
        response = self.client.get(url)
        self.assertEqual(len(response.json()), Character.objects.filter(henchman=True).count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_gadget_list(self):
        url = reverse('gadget_list_api_view')
        response = self.client.get(url)
        self.assertEqual(len(response.json()), Gadget.objects.count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_vehicle_list(self):
        url = reverse('vehicle_list_api_view')
        response = self.client.get(url)
        self.assertEqual(len(response.json()), Vehicle.objects.count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_bond_actor_list(self):
        url = reverse('bond_actor_list_api_view')
        response = self.client.get(url)
        self.assertEqual(len(response.json()), BondActor.objects.count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_movie_retrieve_api_view(self):
        url = reverse('movie_retrieve_api_view', kwargs={'pk': 1})
        response = self.client.get(url)
        serializer = MovieSerializer(Movie.objects.get(pk=1))
        self.assertEqual(response.json(), serializer.data)

    def test_character_retrieve_api_view(self):
        url = reverse('character_retrieve_api_view', kwargs={'pk': 1})
        response = self.client.get(url)
        serializer = CharacterSerializer(Character.objects.get(pk=1))
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse('character_retrieve_api_view', kwargs={'pk': 4})
        response = self.client.get(url)
        serializer = CharacterSerializer(Character.objects.get(pk=4))
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vehicle_retrieve_api_view(self):
        url = reverse('vehicle_retrieve_api_view', kwargs={'pk': 3})
        response = self.client.get(url)
        serializer = VehicleSerializer(Vehicle.objects.get(pk=3))
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_gadget_retrieve_api_view(self):
        url = reverse('gadget_retrieve_api_view', kwargs={'pk': 2})
        response = self.client.get(url)
        serializer = GadgetSerializer(Gadget.objects.get(pk=2))
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_bond_actor_retrieve_api_view(self):
        url = reverse('bond_actor_retrieve_api_view', kwargs={'pk': 1})
        response = self.client.get(url)
        serializer = BondActorSerializer(BondActor.objects.get(pk=1))
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
