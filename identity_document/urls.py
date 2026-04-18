from django.urls import path

from django.urls import path
from .views import add_identity_document

urlpatterns = [
    path('add-new-identity-document/', add_identity_document, name='add_identity_document'),
]