from django.urls import path
from movie.views import ActorView, MovieView, BridgeView

urlpatterns = [
    path('', ActorView.as_view()),
    path('/movies', MovieView.as_view()),
    path('/bridges', BridgeView.as_view())
] 