from django.urls import path
from .views import SnippetListView,SnippetDetailView

urlpatterns = [
    path("snippets/", SnippetListView.as_view(), name="snippets-list"),
    path("snippets/<int:pk>/", SnippetDetailView.as_view(), name="snippets-detail")
]