from django.urls import path
from . import views

urlpatterns = [
    path("post_200_ok/", views.PostOKTemplateView.as_view(), name="post-200-ok"),
]
