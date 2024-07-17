from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add_to_watchlist/", views.add_to_watchlist, name="add_to_watchlist"),
    path(
        "remove_from_watchlist/<int:watchlist_id>/",
        views.remove_from_watchlist,
        name="remove_from_watchlist",
    ),
]
