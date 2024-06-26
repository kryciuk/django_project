from django.urls import path

from recruiter.views import CityCreateView
from recruiter.views.positions import (
    PositionCreateView,
    PositionDeleteView,
    PositionListView,
)

urlpatterns_positions = [
    path("positions/create", PositionCreateView.as_view(), name="positions-create"),
    path("positions/list", PositionListView.as_view(), name="positions-list"),
    path("positions/<int:pk>/delete", PositionDeleteView.as_view(), name="positions-delete"),
]

urlpatterns_cities = [
    path("cities/create", CityCreateView.as_view(), name="city-create"),
]

urlpatterns = [*urlpatterns_positions, *urlpatterns_cities]
