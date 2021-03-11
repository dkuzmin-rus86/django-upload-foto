from django.urls import path
from .views import HomeView, UploadFotoView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/upload_foto/', UploadFotoView.as_view(), name='upload_foto'),
]