
# Routers provide an easy way of automatically determining the URL conf.

from rest_framework import routers
from .viewsets import MoviesViewSet, TypesViewSet

router = routers.DefaultRouter()

router.register( r'movies', MoviesViewSet )
router.register( r'types', TypesViewSet )

