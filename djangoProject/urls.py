"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from djangoProject import settings
# Core Views Import
from core import urls
# Core API Views Import
from core import urls_routers
# Appointments Views Import
from appointments import urls
# Registration Views Import - Sign Up
from registration import urls
# Contact Views Import
from contact import urls
# Blog Views Import
from blog import urls
# 200 Ok Views Import
from helpers import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # DJANGO REGISTRATION URL
    path("accounts/", include("django.contrib.auth.urls")),
    # CORE VIEWS
    path("", include("core.urls")),
    # CORE API VIEWS,
    path("api-auth/", include("core.urls_routers")),
    # Appointments Views Import
    path("medical/", include("appointments.urls")),
    # Registration Views Import
    path("accounts/", include("registration.urls")),
    # Contact Views Import
    path("contact/", include("contact.urls")),
    # Blog Views Import
    path("blog/", include("blog.urls")),
    # 200 Ok Views Import
    path("post_200_ok/", include("helpers.urls")),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)