from django.urls import path

from .views import HomePageView, AboutPageView, SnackDeleteView, SnackCreateView, SnackUpdateView, SnackDetailView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path('<int:pk>/', SnackDetailView.as_view(), name='detail_view'),
    path('new/', SnackCreateView.as_view(), name='create_view'),
    path('<int:pk>/edit', SnackUpdateView.as_view(), name='update_view'),
    path('<int:pk>/delete', SnackDeleteView.as_view(), name='delete_view'),
]
