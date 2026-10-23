import math

from django.db import models

# Create your models here.


class Pet(models.Model):
    """Our beloved pets."""

    class Meta:
        """Pet meta."""

        verbose_name = "Pet"
        verbose_name_plural = "Pets"

    name = models.CharField(max_length=150)
    species = models.CharField(max_length=150)
    hunger_level = models.FloatField()
    bored_level = models.FloatField()
    upset_level = models.FloatField()
    violent_level = models.FloatField()
    sleepy_level = models.FloatField()
    age = models.IntegerField()
    weight = models.IntegerField()
    photo = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100
    )

    def check_upset(self) -> str:
        """Return message refelecting upset level."""
        msg: dict[int, str] = {
            0: f"{self.name} is great.",
            1: f"{self.name} seems ok.",
            2: f"{self.name} is mildly discontent.",
            3: f"{self.name} is very upset.",
        }
        return msg[math.floor(self.upset_level)]

    def check_hungry(self) -> str:
        """Return message refelecting hungry level."""
        msg: dict[int, str] = {
            0: f"{self.name} is full. Thanks for being such a great pet owner!",
            1: f"{self.name} is a bit hungry.",
            2: f"{self.name} is starving. Feed them already!",
            3: f"{self.name} is a bit hungry.",
            4: f"{self.name} is rabidly hungry. Feed them so nobody gets hurt!",
        }
        return msg[math.floor(self.hunger_level)]

    def check_bored(self) -> str:
        """Return message refelecting bored level."""
        msg = {
            0: f"{self.name} is enjoying themselves. Thanks for being such a great pet owner!",
            1: f"{self.name} seems ok.",
            2: f"{self.name} seems a little board.",
            3: f"{self.name} is really bored. Let's entertain them!",
        }
        return msg[math.floor(self.bored_level)]

    def check_violent(self) -> str:
        """Return message refelecting violent level."""
        msg: dict[int, str] = {
            0: f"{self.name} is at peace. Thanks for being such a great pet owner!",
            1: f"{self.name} seems a bit discontent.",
            2: f"{self.name} is grumpy.",
            3: f"{self.name} is giving you a scary look! Help them calm down",
            4: f"{self.name} is out there committing crimes! Watch out for law enforcement.",
        }
        return msg[math.floor(self.violent_level)]

    def check_sleepy(self) -> str:
        """Return message refelecting sleepy level."""
        msg: dict[int, str] = {
            0: f"{self.name} is wide awake.",
            1: f"{self.name} is doing ok.",
            2: f"{self.name} could use a nap.",
            3: f"{self.name} looks a little tired.",
            4: f"{self.name} is falling asleep standing up! Better put them to bed.",
        }
        return msg[math.floor(self.violent_level)]

    def adjust_value(self, field, amt=1):
        """Improve the attribute's state."""
        field += amt
        self.save()

    def interact(self, action: str, amt=1):
        """Interact with your pet and affect the related attribute."""
        if action == "ignore":
            self.upset_level += 0.5
            self.bored_level += 0.5
        elif action == "throw":
            self.upset_level += 1
            self.violent_level += 2
            self.bored_level -= 2
        elif action == "talk":
            self.bored_level -= 1
            self.hunger_level += 1
        else:
            actions: dict[str, float] = {
                "feed": self.hunger_level,
                "pet": self.upset_level,
                "play": self.bored_level,
            }
            self.adjust_value(actions[action], amt)
        self.save()

    def __str__(self) -> str:
        return str(self.name)


class Player(models.Model):
    """Our beloved pets."""

    class Meta:
        """Pet meta."""

        verbose_name = "Pet"
        verbose_name_plural = "Pets"

    name = models.CharField(max_length=150)
