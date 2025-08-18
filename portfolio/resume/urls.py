from django.urls import path
from resume.views import home

  # For URL namespacing

urlpatterns = [
    path('', home, name='home'),
    # You can add more paths here as your project grows
]