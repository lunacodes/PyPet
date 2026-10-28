from django.contrib import admin

from .models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "species",
        "hunger_level",
        "bored_level",
        "upset_level",
        "violent_level",
        "sleepy_level",
        "age",
        "weight",
        "photo",
    )


# Register your models here.

admin.site.register(Pet, PetAdmin)
