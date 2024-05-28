from django.urls import path
from . import views

urlpatterns = [
    path('pull_document/<str:document_id>/', views.pull_document, name='pull_document'),
    path('documents/', views.document_list, name='document_list'),
]
