from django.urls import path
from .views import ListJobOffer , joboffer_detail
urlpatterns = [
    path('joboffer/',ListJobOffer.as_view()),
    path('joboffer/<int:pk>',joboffer_detail.as_view())
]