from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostOKTemplateView.as_view(), name="post-200-ok"), # -> 202 Ok URL
]
