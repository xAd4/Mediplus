from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name="home"),
    path('blog/', views.BlogTemplateView.as_view(), name="blog"),
    path("post_200_ok/", views.PostOKTemplateView.as_view(), name="post-200-ok"),
]
