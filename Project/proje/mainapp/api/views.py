from django.shortcuts import render

from .models import Article,Writer,Student,School

from .serializers import ArticleSerializers,WriterSerializers,SchoolSerializers,StudentSerializers

from rest_framework.views import APIView
from rest_framework import request, response
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import viewsets
import time
from .add import adding_log
from datetime import datetime




class ArticleAPIView(APIView):
    def get_queryset(self):
        articles = Article.objects.all()
        return articles

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        request.start_time = time.time()
        timestamp = request.start_time
        try:
            id = kwargs['id']
            if id != None:
                articles = Article.objects.get(id=id)
                serializer = ArticleSerializers(articles)
                
        except:

            artciles = self.get_queryset()
            serializer = ArticleSerializers(artciles, many=True)

        end_time = (time.time() - request.start_time)*1000
        
        current_time = now.strftime("%H:%M")
        adding_log(request.method,end_time,timestamp,current_time)
        

        return Response(serializer.data)

    def post(self, request):
        request.start_time = time.time()
        timestamp = request.start_time
        serilazer = ArticleSerializers(data=request.data)

        if serilazer.is_valid():
            serilazer.save()
            end_time = (time.time() - request.start_time)*1000
            adding_log(request.method, end_time, timestamp)
            return Response(serilazer.data, status=status.HTTP_201_CREATED)
        return Response(serilazer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        article = Article.objects.get(id=id)
        request.start_time = time.time()
        timestamp = request.start_time
        serializer = ArticleSerializers(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            end_time = (time.time() - request.start_time)*1000
            adding_log(request.method, end_time, timestamp)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        request.start_time = time.time()
        timestamp = request.start_time
        article = Article.objects.get(id=id)
        article.delete()
        end_time = (time.time() - request.start_time)*1000
        adding_log(request.method, end_time, timestamp)
        return Response(status=status.HTTP_204_NO_CONTENT)


class WriterAPIView(APIView):
    def get_queryset(self):
        writers = Writer.objects.all()
        return writers

    def get(self, request, *args, **kwargs):
        request.start_time = time.time()
        timestamp = request.start_time
        try:
            id = kwargs['id']
            if id != None:

                writers = Writer.objects.get(id=id)
                serializer = WriterSerializers(writers)
        except:

            writers = self.get_queryset()
            serializer = WriterSerializers(writers, many=True)

        end_time = (time.time() - request.start_time)*1000
        adding_log(request.method, end_time, timestamp)
        return Response(serializer.data)

    def post(self, request):
        request.start_time = time.time()
        timestamp = request.start_time
        serilazer = WriterSerializers(data=request.data)

        if serilazer.is_valid():
            serilazer.save()
            end_time = (time.time() - request.start_time)*1000
            adding_log(request.method, end_time, timestamp)
            return Response(serilazer.data, status=status.HTTP_201_CREATED)
        return Response(serilazer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        writer = Writer.objects.get(id=id)
        request.start_time = time.time()
        timestamp = request.start_time
        serializer = WriterSerializers(writer, data=request.data)

        if serializer.is_valid():
            serializer.save()
            end_time = (time.time() - request.start_time)*1000
            adding_log(request.method, end_time, timestamp)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        request.start_time = time.time()
        timestamp = request.start_time
        writer = Writer.objects.get(id=id)
        writer.delete()
        end_time = (time.time() - request.start_time)*1000
        adding_log(request.method, end_time, timestamp)
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentAPIView(APIView):
    def get_queryset(self):
        students = Student.objects.all()
        return students

    def get(self, request, *args, **kwargs):
        request.start_time = time.time()
        timestamp = request.start_time
        try:
            id = kwargs['id']
            if id != None:

                students = Student.objects.get(id=id)
                serializer = StudentSerializers(students)
        except:

            students = self.get_queryset()
            serializer = StudentSerializers(students, many=True)
        end_time = (time.time() - request.start_time)*1000
        adding_log(request.method, end_time, timestamp)
        return Response(serializer.data)

    def post(self, request):
        request.start_time = time.time()
        timestamp = request.start_time
        serilazer = StudentSerializers(data=request.data)

        if serilazer.is_valid():
            serilazer.save()
            end_time = (time.time() - request.start_time)*1000
            adding_log(request.method, end_time, timestamp)
            return Response(serilazer.data, status=status.HTTP_201_CREATED)
        return Response(serilazer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        student = Student.objects.get(id=id)
        request.start_time = time.time()
        timestamp = request.start_time
        serializer = StudentSerializers(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            end_time = (time.time() - request.start_time)*1000
            adding_log(request.method, end_time, timestamp)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        request.start_time = time.time()
        timestamp = request.start_time
        student = Student.objects.get(id=id)
        student.delete()
        end_time = (time.time() - request.start_time)*1000
        adding_log(request.method, end_time, timestamp)
        return Response(status=status.HTTP_204_NO_CONTENT)


class SchoolAPIView(APIView):
    def get_queryset(self):
        schools = School.objects.all()
        return schools

    def get(self, request, *args, **kwargs):
        request.start_time = time.time()
        timestamp = request.start_time
        try:
            id = kwargs['id']
            if id != None:

                schools = School.objects.get(id=id)
                serializer = SchoolSerializers(schools)
        except:

            schools = self.get_queryset()
            serializer = SchoolSerializers(schools, many=True)
        end_time = (time.time() - request.start_time)*1000
        adding_log(request.method, end_time, timestamp)
        return Response(serializer.data)

    def post(self, request):
        request.start_time = time.time()
        timestamp = request.start_time
        serilazer = SchoolSerializers(data=request.data)

        if serilazer.is_valid():
            serilazer.save()
            end_time = (time.time() - request.start_time)*1000
            adding_log(request.method, end_time, timestamp)
            return Response(serilazer.data, status=status.HTTP_201_CREATED)
        return Response(serilazer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        request.start_time = time.time()
        timestamp = request.start_time
        school = School.objects.get(id=id)
        serializer = SchoolSerializers(school, data=request.data)

        if serializer.is_valid():
            serializer.save()
            end_time = (time.time() - request.start_time)*1000
            adding_log(request.method, end_time, timestamp)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        request.start_time = time.time()
        timestamp = request.start_time
        school = School.objects.get(id=id)
        school.delete()
        end_time = (time.time() - request.start_time)*1000
        adding_log(request.method, end_time, timestamp)
        return Response(status=status.HTTP_204_NO_CONTENT)
