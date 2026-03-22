from django.urls import path
from .views import LanguagesListView, LanguageDetailView

urlpatterns = [
    path("language/",LanguagesListView.as_view(),name="languages-list"),
    path("language/<int:pk>/",LanguageDetailView.as_view(),name="language-detail")
]
