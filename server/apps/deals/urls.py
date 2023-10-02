from django.urls import path

from .views import DealsCreate, DealsGet

urlpatterns = [
    path('deals-upload/', DealsCreate.as_view()),
    path('deals-get/', DealsGet.as_view()),
]
