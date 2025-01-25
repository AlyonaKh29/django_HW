from django.urls import path

from measurement.views import SensorView, SensorUpdateView, MeasurementsView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SensorUpdateView.as_view()),
    path('measurements/', MeasurementsView.as_view()),
]
