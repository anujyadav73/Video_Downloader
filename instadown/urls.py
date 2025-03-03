from django.urls import path
from .views import download_video,landing_page

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('download/', download_video, name='download_video'),
#    path('success/', download_video, name='success'),
]