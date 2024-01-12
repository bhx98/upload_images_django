from django.urls import path

from upload import views
# from .views import image_upload_view
urlpatterns = [
    path('upload/', views.image_upload_view),
    path('',views.show_images),
]

