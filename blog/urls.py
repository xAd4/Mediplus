from django.urls import path
from . import views

urlpatterns = [
    # POST LIST
    path('', views.PostListView.as_view(), name="blog"),
    # POST DETAIL
    path('<int:pk>/', views.PostDetailView.as_view(), name="blog-detail"),
    # COMMENTS
    path("delete/<int:pk>/", views.CommentDeleteView.as_view(), name="blog-detail-delete"),
    # POST CRUD
    path("post/create/", views.PostCreateView.as_view(), name="blog-create"),
    path("post/update/<int:pk>/", views.PostUpdateView.as_view(), name="blog-update"),
    path("post/delete/<int:pk>/", views.PostDeleteView.as_view(), name="blog-delete"),
]
