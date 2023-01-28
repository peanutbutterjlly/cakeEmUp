from django.urls import path

from .views import FormView, GalleryView, IndexView, PricingView

app_name: str = "bakery"

urlpatterns: list = [
    path("", IndexView.as_view(), name="home"),
    path("gallery/", GalleryView.as_view(), name="gallery"),
    path("form/", FormView.as_view(), name="form"),
    path(
        "pricing/",
        PricingView.as_view(),
        name="pricing",
    ),
]
