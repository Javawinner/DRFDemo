from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Book,Publisher
import json
from django.core import serializers

# Create your views here.
# book_list = [
#     {
#        id: 1,
#        "title": "xx",
#
#     }
#
# ]

# class BookView(View):
#     def get(self, request):
#         book_queryset = Book.objects.values("id", "title", "pub_time",'publisher')
#         book_list = list(book_queryset)
#         # ret = json.dumps(book_list, ensure_ascii=False)
#         # return HttpResponse(ret)
#         ret=[]
#         for book in book_list:
#             print(book)
#             book['publisher'] = {
#                 'id': book['id'],
#                 'title': Publisher.objects.filter(id=book['publisher']).first().title
#             }
#             ret.append(book)
#         return JsonResponse(ret, safe=False, json_dumps_params={"ensure_ascii": False})

class BookView(View):
    def get(self,request):
        book_queryset = Book.objects.all()
        data = serializers.serialize("json",book_queryset, ensure_ascii=False)
        return HttpResponse(data)
