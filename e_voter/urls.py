from django.urls import path, include
from rest_framework.routers import SimpleRouter

from e_voter import views

router = SimpleRouter()
router.register('voters', views.VotersRoute)

urlpatterns = [
    path('explore/', include(router.urls)),
]
