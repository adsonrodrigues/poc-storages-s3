from rest_framework import routers
from docs.views import DocumentViewset

router = routers.SimpleRouter()

router.register(r'docs', DocumentViewset)

urlpatterns = []

urlpatterns += router.urls
