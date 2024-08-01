from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name="home"),
    path('portfolio/', views.PortfolioTemplateView.as_view(), name="portfolio"),
    path("post_200_ok/", views.PostOKTemplateView.as_view(), name="post-200-ok"),
]
