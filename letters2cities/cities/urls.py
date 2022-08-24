from django.urls import path
from . import views

app_name = "cities"
urlpatterns = [
    # e.g. /
    path("", views.CityListView.as_view(), name="city_list"),
    # e.g. /1/
    path("<int:pk>/", views.CityDetailView.as_view(), name="city_detail"),
    # e.g. /1/write_letter
    path("<int:pk>/write_letter", views.write_letter)
]
handler404 = 'cities.views.page_not_found'
