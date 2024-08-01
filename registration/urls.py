from django.urls import path
from . import views as registration_views
urlpatterns = [
 # Otras rutas de tu aplicación
 path("signup/", registration_views.SignUpView.as_view(), name="signup"),
]
