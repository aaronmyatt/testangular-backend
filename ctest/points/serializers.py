from rest_framework import serializers
from .models import Points

class PointsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Points