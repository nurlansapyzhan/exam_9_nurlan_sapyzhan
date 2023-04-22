from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from app.forms import PhotoForm
from app.models import PhotoModel


# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    model = PhotoModel
    context_object_name = 'photos'
    ordering = ['-created_at']


class PhotoDetailView(DetailView):
    template_name = 'photo_detail.html'
    model = PhotoModel

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        photo = PhotoModel.objects.all().filter(photo=self.object.pk)
        kwargs['photo'] = photo
        return super().get_context_data(**kwargs)


class PhotoUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'update_photo.html'
    form_class = PhotoForm
    model = PhotoModel

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        user = self.request.user
        photo = self.get_object()
        return user == photo.author or self.request.user.has_perm('change_photomodel')


class PhotoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'delete_photo.html'
    model = PhotoModel
    context_object_name = 'photo'
    success_url = reverse_lazy('index')

    def test_func(self):
        user = self.request.user
        post = self.get_object()
        return user == post.author or self.request.user.has_perm('delete_photomodel')


class AddPhotoView(LoginRequiredMixin, CreateView):
    model = PhotoModel
    fields = ['photo', 'description']
    template_name = 'add_photo.html'

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.author = self.request.user
        photo.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')
