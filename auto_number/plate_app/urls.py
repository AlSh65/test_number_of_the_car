from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import PlateGenerateView, PlateGetView, PlateAddView

router = SimpleRouter()
router.register(r'plate', PlateGenerateView, basename='generate')
router.register(r'plate', PlateGetView, basename='get')
router.register(r'plate', PlateAddView, basename='add')

urlpatterns = [
    path('', include(router.urls)),
]
