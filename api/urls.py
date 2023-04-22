from django.urls import path

from api.views import AddToFavorite

urlpatterns = [
    path('favorites/add/<int:pk>/', AddToFavorite.as_view(), name='add_to_favorite')
]
