from django.contrib import admin
from django.urls import include, path
from pets import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"pets", views.PetView, "pet")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
