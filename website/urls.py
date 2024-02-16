from django.urls import path
from . import views


urlpatterns = [ 
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    # path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('record/<int:pk>',views.Customer_record,name='record'),
    path('delete_record/<int:pk>',views.delete_record,name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>',views.update_record,name='update_record'),
]