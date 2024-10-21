from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home),
    path('', views.HomeView.as_view()),
    path('authorized/', views.authorized)
]