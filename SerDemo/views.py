from django.shortcuts import render
from rest_framework.views import APIView
from djangoDemo.models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
# Create your views here.

class BookView(APIView):
    def get(self, request):
        book_queryset = Book.objects.all()
        # 用序列化器进行序列化
        ser_obj = BookSerializer(book_queryset, many=True)
        return Response(ser_obj.data)

    def post(self, request):
        # 确定数据类型以及数据以及数据结构
        # 对前端的数据进行校验
        book_obj = request.data
        ser_obj = BookSerializer(data=book_obj)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.validated_data)
        return Response(ser_obj.errors)



class BookEditView(APIView):
    def get(self, request, id):
        book_obj = Book.objects.filter(id=id).first()
        ser_obj = BookSerializer(book_obj)
        return Response(ser_obj.data)

    def put(self, request, id):
        book_obj = Book.objects.filter(id=id).first()
        # partial=True  对序列化器中的update方法中, 只对部分字段进行校验
        ser_obj = BookSerializer(instance=book_obj, data=request.data, partial=True)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.validated_data)
        return Response(ser_obj.errors)



