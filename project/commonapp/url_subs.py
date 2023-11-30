from django.urls import path
from .views import IndexView
from .views import subscriptions
urlpatterns = [
   path('', subscriptions, name='subscriptions'),
    path('s/', IndexView.as_view()),
]


