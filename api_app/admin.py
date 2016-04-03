from django.contrib import admin
from api_app import models


admin.site.register(
        [
            models.Character, models.Vehicle, models.Gadget,
            models.BondActor, models.Movie
            ]
        )
