from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name="home"),
    path('portfolio/', views.PortfolioTemplateView.as_view(), name="portfolio"),
    path('blog/', views.BlogTemplateView.as_view(), name="blog"),
    path('contact/', views.ContactTemplateView.as_view(), name="contact"),
]
