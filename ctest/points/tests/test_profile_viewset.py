from django.core.urlresolvers import resolve, reverse
from test_plus.test import TestCase

from ..views import PointsViewSet

def test_url_success():
    view = resolve('/api/v1/points/')
    assert view.func.__name__ == PointsViewSet.__name__