from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)

urlpatterns = [
    #path('', admin.site.urls),
    path('', include(router.urls))
]
