from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('home/',views.home,name="home"),
    path('registerjobseeker/',views.registerjobseeker,name="jobseeker reg"),
    path('follow-employee/',views.follow_employee,name="follow employee"),
    path('messages/',views.mymsg,name="notification"),
    path('search/',views.search,name="querysearch"),
    path('handle_comment/',views.handlecomment,name="comment-publish"),
    path('handlelove/',views.lovepost,name="postlove"),
    path('profile/',views.profile,name="manage profile"),
    path('edit_profile/',views.editprofile,name="edit profile"),
    path('handlelogout/',views.handlelogout,name="logout"),
    path('myjobs/',views.myjobs,name="shortlisted jobs"),
]
