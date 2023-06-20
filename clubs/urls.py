from django.urls import path
from .views import (ClubListView, ClubDetailView, ClubCreateView, ClubUpdateView, ClubDeleteView)

urlpatterns = [
    path('snack/', ClubListView.as_view(), name='club_list'),
    path('snack/<int:pk>/', ClubDetailView.as_view(), name='club_detail'),
    path('snack/create/', ClubCreateView.as_view(), name='club_create'),
    path('snack/<int:pk>/update/', ClubUpdateView.as_view(), name='club_update'),
    path('snack/<int:pk>/delete/', ClubDeleteView.as_view(), name='club_delete'),
]