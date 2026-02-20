from django.urls import path

from .views import home, about, contact,product_page, landing_page

urlpatterns = [
    path("", home, name="home_page"),
    path("about/", about, name="about_page"),
    path("product/", product_page, name="product_page"),
    path("contact/", contact, name="contact_page"),
    path("landing/", landing_page, name="landing_page"),
]
