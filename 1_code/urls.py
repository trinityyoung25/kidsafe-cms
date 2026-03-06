from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("upload/", views.upload_content, name="upload"),
    path("library/", views.child_library, name="library"),
]
