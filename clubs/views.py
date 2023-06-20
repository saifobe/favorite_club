from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Club


class ClubListView(ListView):
    template_name = "clubs/club-list.html"
    model = Club


class ClubDetailView(DetailView):
    template_name = "clubs/club-detail.html"
    model = Club


class ClubCreateView(CreateView):
    template_name = "clubs/club-create.html"
    model = Club
    fields = ['name','fan','details']


class ClubUpdateView(UpdateView):
    template_name = "clubs/club-update.html"
    model = Club
    fields = ['name','fan','details']


class ClubDeleteView(DeleteView):
    template_name = "clubs/club-delete.html"
    model = Club
    success_url = reverse_lazy("club_list")