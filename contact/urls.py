from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactTemplateView.as_view(), name="contact"),
]
