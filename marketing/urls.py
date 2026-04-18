from django.urls import path
from . import views

app_name = 'marketing'

urlpatterns = [
    path('', views.index, name='index'),
    path('AddNewCoupon', views.add_coupon, name='add_coupon'),
    path('AddNewCouponUsage', views.add_coupon_usage, name='add_coupon_usage'),
    path('AddNewReview', views.add_review, name='add_review'),
]
