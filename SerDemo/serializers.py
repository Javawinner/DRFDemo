from rest_framework import serializers
from djangoDemo.models import Book
import copy


class PublishSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=32)


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=32)

'''自定义校验'''
# def my_validate(value):
#     print('11111111')
#     if '敏感信息' in value.lower():
#         raise serializers.ValidationError('有敏感词汇')
#
#     return value
#
# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(required=False)
#     title = serializers.CharField(max_length=32, validators=[my_validate, ])
#     pub_time = serializers.DateField()
#
#     # read_only=True  反序列化不校验该字段, 序列化时校验该字段
#     category = serializers.CharField(source="get_category_display", read_only=True)
#
#     # 外键关系
#     publisher = PublishSerializer(read_only=True)
#     # 内部通过外键关系的id找到了publish_obj
#     # PublishSerializer(publish_obj)
#     authors = AuthorSerializer(many=True, read_only=True)
#
#     # write_only=True  序列化时候不校验该字段, 反序列化校验该字段
#     post_category = serializers.IntegerField(write_only=True)
#     publisher_id = serializers.IntegerField(write_only=True)
#     author_list = serializers.ListField(write_only=True)
#
#     def create(self, validated_data):
#         # validated_data  校验通过的数据  就是book_obj
#         # 通过ORM操作给Book表增加数据
#         print(validated_data)
#         '''
#         前端传过来的数据:
#         {'title': '水货开房没带身份证',
#          'pub_time': datetime.date(2019, 10, 8),
#          'post_category': 1,
#          'publisher_id': 1,
#          'author_list': [1, 2]}
#         '''
#         cleaned_data = copy.deepcopy(validated_data)
#         cleaned_data.pop('author_list')
#         cleaned_data['category'] = cleaned_data['post_category']
#         cleaned_data.pop('post_category')
#         book_obj = Book.objects.create(**cleaned_data)
#         book_obj.authors.add(*validated_data['author_list'])
#         return book_obj
#
#     def update(self, instance, validated_data):
#         # instance 更新的book_obj 对象
#         # validated_data  前端传过来的并且校验通过的数据
#         # validated data中的键值肯定是 title|pub_time|post_category|publisher_id|author_list|
#         # ORM 做更新操作
#         instance.title = validated_data.get('title', instance.title)
#         instance.pub_time = validated_data.get('pub_time', instance.pub_time)
#         instance.category = validated_data.get('post_category', instance.category)
#         instance.publisher_id = validated_data.get('publisher_id', instance.publisher_id)
#         if validated_data.get('author_list'):
#             instance.author.set(validated_data['author_list'])
#         instance.save()
#
#         return instance
#
#     '''单个字段校验'''
#     def validate_title(self, value):
#         print(22222222)
#         # value就是title的值
#         if 'python' not in value.lower():
#             raise serializers.ValidationError("标题必须含有python")
#         return value
#
#
#     '''多个字段校验'''
#     def validate(self, attrs):
#         print(333333333333)
#         # attrs  字典有你传过来的所有字段
#         print(attrs)
#         if "python" in attrs['title'].lower() and attrs['post_category'] == 1:
#             return attrs
#         else:
#             raise serializers.ValidationError('分类或标题不符合要求')



class BookSerializer(serializers.ModelSerializer):

    category_display = serializers.SerializerMethodField()
    publishers_info = serializers.SerializerMethodField()
    author_info = serializers.SerializerMethodField()

    def get_category_display(self, obj):
        # obj 就是序列化的每个book 对象
        # print('obj', obj)
        return obj.get_category_display()

    def get_publishers_info(self, obj):
        publsher_obj = obj.publisher
        return {'id': publsher_obj.id, 'name': publsher_obj.title}

    def get_author_info(self, obj)
        author_obj = obj.authors.all()
        return [{'id': author.pk, 'name': author.name} for author in author_obj]


    class Meta:
        model = Book

        # fileds指定字段, __all__显示所有字段, exclude排除字段,  fields和exclude 不能共存, 只能指定一个
        fields = '__all__'
        # exclude = ['id']
        # depth = 1 会将所有的外键字段加上选项 read_only = True, 并且会拿到所有字段, 一般在开发中不用
        # depth = 1
        extra_kwargs = {"publisher": {"write_only": True}, "author": {"write_only": True}}