from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name="blog"),
    path('<int:pk>/', views.PostDetailView.as_view(), name="blog-detail"),
    path("delete/<int:pk>/", views.CommentDeleteView.as_view(), name="blog-detail-delete"),
]
