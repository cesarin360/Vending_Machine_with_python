from django.urls import path
from .views import *

urlpatterns = [
    path('', store, name="store"),
    path('pagination/', pagination, name="pagination"),
    path('checkout/', checkout, name="checkout"),
    path('restar_100/', restar_100, name="restar_100"),
    path('restar_50/', restar_50, name="restar_50"),
    path('restar_20/', restar_20, name="restar_20"),
    path('restar_10/', restar_10, name="restar_10")
]

