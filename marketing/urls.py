from django.urls import path
from . import views

app_name = 'marketing'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.marketing_login, name='login'),
    path('logoff/', views.marketing_logoff, name='logoff'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('add-new-record/', views.add_new_record, name='add_new_record'),
    path('AddNewCoupon/', views.add_coupon, name='add_coupon'),
    path('AddNewCouponUsage/', views.add_coupon_usage, name='add_coupon_usage'),
    path('AddNewReview/', views.add_review, name='add_review'),
]
