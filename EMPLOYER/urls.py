from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('home/',views.home,name="home"),
    path('registeremployer/',views.registeremployer,name="register employer"),
    path('publish-post/',views.publishpost,name="publish post"),
    path('my-jobs/',views.myjobs,name="my jobs"),
    path('publish-jobs/',views.publishjobs,name="publish job"),
    path('delete-job/',views.deletejob,name="delete-job"),
    path('applied-candidate/',views.candidateapplied,name="candidates application"),
    path('shortlisted-candidate/',views.candidateshortlisted,name="shortlisted candidate"),
    path('release-user/',views.releaseuser,name="releaseuser"),
    path('accept-user/',views.acceptuser,name="shortlist"),
    path('reject-user/',views.rejectuser,name="rejectuser"),
    path('receive-response/<str:slug>/<int:id>/',views.receiveresponse,name="receive response"),
    path('delete-article/article/<int:id>/',views.deletepost,name="delete_post"),
    path('handlelogout/',views.handlelogout,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('edit_profile/',views.editprofile,name="edit profile"),
]
