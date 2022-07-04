from django.urls import path

from .views import DogView, OwnerView

urlpatterns = [
    path('', OwnerView.as_view()),
    path('/dogs', DogView.as_view()),
] 