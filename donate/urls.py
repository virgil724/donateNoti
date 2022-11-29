from django.urls import path, include
from .views import StreamerAPIViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"streamer", StreamerAPIViewSet, basename="streamer")
urlpatterns = [path("api/", include(router.urls))]
# path("streamer/<str:deleteKey>/", StreamerAPIView.as_view()),
# path("streamer/", CreateStreamerAPIView.as_view()),
"""
router.urls
[
    <URLPattern '^streamer/$' [name='streamer-list']>,
    <URLPattern '^streamer\.(?P<format>[a-z0-9]+)/?$' [name='streamer-list']>,
    <URLPattern '^streamer/(?P<deleteKey>[^/.]+)/$' [name='streamer-detail']>,
    <URLPattern '^streamer/(?P<deleteKey>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='streamer-detail']>,
    <URLPattern '^$' [name='api-root']>,
    <URLPattern '^\.(?P<format>[a-z0-9]+)/?$' [name='api-root']>
]
"""
