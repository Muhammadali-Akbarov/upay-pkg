from django.urls import path

from .views import RegCardView

urlpatterns: list = []

urlpatterns += [
    path('reg-card/', RegCardView.as_view())
]
