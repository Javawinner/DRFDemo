from django.test import TestCase

# Create your tests here.
book_obj = {
    "title": "水货开房没带身份证",
    "pub_time": "2019-10-08",
    "post_category": 1,
    "publisher_id": 1,
    "author_list": [1, 2]
}

book_obj.pop('author_list')
print(book_obj)