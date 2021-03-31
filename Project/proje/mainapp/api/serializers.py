from .models import Article,Writer,Student,School

from rest_framework import serializers


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class WriterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = '__all__'


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class SchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
