from django.db import models

class Points(models.Model):
    user = models.ForeignKey("users.User")
    lat = models.DecimalField(decimal_places=4, max_digits=10)
    lng = models.DecimalField(decimal_places=4, max_digits=10)
    note = models.TextField()

