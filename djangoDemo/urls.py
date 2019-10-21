from django.conf.urls import url
from .views import BookView

urlpatterns=[
    url(r'^book', BookView.as_view())
]