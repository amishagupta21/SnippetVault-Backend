from django.urls import path
from .views import TagsListView,TagsDetailsView

urlpatterns=[
    path("tags/",TagsListView.as_view(),name="tags-list"),
    path("tags/<int:pk>/",TagsDetailsView.as_view(),name="tags-details")
]