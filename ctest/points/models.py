from django.db import models

class Points(models.Model):
    user = models.ForeignKey("users.User")
    username = models.TextField()
    email = models.EmailField()
    latest_point_lat = models.DecimalField(decimal_places=4, max_digits=10)
    latest_point_lng = models.DecimalField(decimal_places=4, max_digits=10)
    mapper = models.BooleanField()

