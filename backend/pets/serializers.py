from rest_framework import serializers

from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    """Pet Serializer."""

    class Meta:
        """Pet Serializer meta."""

        model = Pet
        fields = (
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
