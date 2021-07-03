from rest_framework import mixins, viewsets

from docs.models import Document
from docs.serializers import DocumentSerializer


class DocumentViewset(mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
