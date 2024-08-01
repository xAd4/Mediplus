from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogTemplateView.as_view(), name="blog"),
]
