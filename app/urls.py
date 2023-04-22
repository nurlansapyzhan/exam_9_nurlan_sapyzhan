from django.urls import path

from app.views import IndexView, PhotoDetailView, AddPhotoView, PhotoUpdateView, PhotoDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/<int:pk>', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/create', AddPhotoView.as_view(), name='add_photo'),
    path('photo/update/<int:pk>', PhotoUpdateView.as_view(), name='update_photo'),
    path('photo/delete/<int:pk>', PhotoDeleteView.as_view(), name='delete_photo')
]
