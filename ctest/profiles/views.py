from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import Points
from .permissions import IsOwnerOrReadOnly
from .serializers import PointsSerializer


class PointsViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives User accounts
    """
    queryset = Points.objects.all()
    serializer_class = PointsSerializer
    permission_classes = (IsOwnerOrReadOnly,)