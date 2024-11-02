from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("vote/<int:item_id>/", views.vote, name="vote"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
