from django.db import models

class BaseUser(models.Model):
    id = models.CharField(
        unique=True,
        primary_key=True,
        blank=False,
        null=False,
        max_length=10
    )

    password_hash = models.CharField(
        blank=False,
        null=False,
        max_length=128
    )

    create_date = models.DateTimeField(
        auto_now=True,
        blank=False,
        null=False
    )

# class SmallToken(models.Model):
#     user = models.ForeignKey(
#         BaseUser,
#         on_delete=models.CASCADE,
#     )
#
#     salt = models.CharField(
#         blank=False,
#         null=False,
#         max_length=32
#     )
#
#     create_date = models.DateTimeField(
#         auto_now=True,
#         blank=False,
#         null=False
#     )
#
#     #TODO: put in setting or db
#     life_hour = 1