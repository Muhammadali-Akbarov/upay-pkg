from django.urls import path

from .views import RegCardView
from .views import CreateHoldView
from .views import PayHoldView
from .views import CheckHoldView
from .views import CancelHoldView

urlpatterns: list = []

urlpatterns += [
    path('reg-card/', RegCardView.as_view()),
    path('create-hold/', CreateHoldView.as_view()),
    path('pay-hold/', PayHoldView.as_view()),
    path('check-hold/', CheckHoldView.as_view()),
    path('cancel-hold/', CancelHoldView.as_view()),
]
