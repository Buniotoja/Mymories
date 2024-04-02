from django.urls import path
from .views import MemoryView, PostView, PictureView


urlpatterns = [
    path('memory/', MemoryView.get_list),
    path('memory/<int:pk>/', MemoryView.get_detail),
    path('memory/<int:fk>/post/', PostView.get_list),
    path('memory/<int:fk>/post/<int:pk>/', PostView.get_detail),
    path('memory/<int:fk>/picture/', PictureView.get_list),
    path('memory/<int:fk>/picture/<int:pk>/', PictureView.get_detail)
]
