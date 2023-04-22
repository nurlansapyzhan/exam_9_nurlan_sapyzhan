from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import PhotoModel


class AddToFavorite(APIView):
    def post(self, request, pk):
        photo = get_object_or_404(PhotoModel, pk=pk)
        user = request.user
        if user in photo.favorite.all():
            photo.favorite.remove(user)
            photo.save()
            return Response({"favorite_info": "Removed from favorite"})
        else:
            photo.favorite.add(user)
            photo.save()
            return Response({"favorite_info": "Added to favorite"})
