from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

from .views import NoteViewSet
from .views import NoteList
app_name = 'user'

router = DefaultRouter()
router.register('profile',views.ProfileViewSet)
router.register('note', views.NoteViewSet)
router.register('post', views.PostViewSet)
router.register('comment', views.CommentViewSet)



urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('myprofile/', views.MyProfileListView.as_view(), name='myprofile'),
    path('note/get/pending/', views.NoteList.as_view(), name='note-pending-list'),
    path('',include(router.urls))

]


