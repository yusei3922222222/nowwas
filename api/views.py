from datetime import timezone
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from . import serializers
from .models import Profile, Post, Comment
from .models import Note
from .serializers import NoteSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(userProfile=self.request.user)


class MyProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

    def get_queryset(self):
        return self.queryset.filter(userProfile=self.request.user)

class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the notes that are not expired (created within the last 5 minutes)
        return Note.objects.filter(
            usernote=self.request.user,
            created_on__gte=timezone.now() - timezone.timedelta(minutes=5)
        )

    def perform_create(self, serializer):
        serializer.save(usernote=self.request.user)

# NoteViewSetの実装を追加（詳細ページにも5分経過の制約を追加）
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the notes that are not expired (created within the last 5 minutes)
        return Note.objects.filter(
            usernote=self.request.user,
            created_on__gte=timezone.now() - timezone.timedelta(minutes=5)
        )

    def perform_create(self, serializer):
        serializer.save(usernote=self.request.user)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(userPost=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def perform_create(self, serializer):
        serializer.save(userComment=self.request.user)


from django.shortcuts import render

# Create your views here.
