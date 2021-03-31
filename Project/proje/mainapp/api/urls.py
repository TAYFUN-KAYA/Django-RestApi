
from .views import ArticleAPIView,WriterAPIView,StudentAPIView,SchoolAPIView
from django.urls import path, include

urlpatterns = [
    
    path('article/', ArticleAPIView.as_view()),
    path('article/<int:id>/', ArticleAPIView.as_view()),

    path('writer/',WriterAPIView.as_view()),
    path('writer/<int:id>/',WriterAPIView.as_view()),

    path('student/',StudentAPIView.as_view()),
    path('student/<int:id>/',StudentAPIView.as_view()),

    path('school/', SchoolAPIView.as_view()),
    path('school/<int:id>/', SchoolAPIView.as_view()),
]
