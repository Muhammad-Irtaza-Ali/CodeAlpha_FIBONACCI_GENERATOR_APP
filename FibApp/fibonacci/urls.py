from django.urls import path
from .views import fibonacci_view  # Import the view that generates the Fibonacci sequence

urlpatterns = [
    path('', fibonacci_view, name='fibonacci'),  # Map the main page to the fibonacci_view function
]
