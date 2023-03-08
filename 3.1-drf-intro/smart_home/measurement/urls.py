from django.urls import path

from measurement.views import SensorsViews, MeasurementsView, SensorView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsViews.as_view()),
    path('sensor/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementsView.as_view()),
]
