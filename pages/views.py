from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy


class HomePageView(ListView):
    template_name = "pages/home.html"
    model = Snack
    context_object_name = 'snacks'


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class SnackDetailView(DetailView):
    template_name = 'CRUD/snack-detail.html'
    model = Snack


class SnackCreateView(CreateView):
    template_name = 'CRUD/snack-create.html'
    model = Snack
    fields = ['title', 'description', 'purchaser']


class SnackUpdateView(UpdateView):
    template_name = 'CRUD/snack-update.html'
    model = Snack
    fields = ['title', 'description', 'purchaser']


class SnackDeleteView(DeleteView):
    template_name = 'CRUD/snack-delete.html'
    model = Snack
    success_url = reverse_lazy('home')
