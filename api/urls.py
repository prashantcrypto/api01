from django.urls import path
from api import views
from .views import get_data, post_data, walletDetail, TwitterLinkUpdate

urlpatterns = [
    path('getall', get_data.as_view(), name='get_data'),
    path('putdata', post_data.as_view(), name='post_data'),
    path('userdata/<str:wallet_address>/',
         walletDetail.as_view(), name='wallet_detail'),
    path('removetwitter/<str:wallet_address>',
         TwitterLinkUpdate.as_view(), name='Twitter-link-update'),
]
