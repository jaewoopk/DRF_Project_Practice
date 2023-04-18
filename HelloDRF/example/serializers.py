from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer) : # --> 최신 방법
    class Meta :
        model = Book
        fields = ['bid', 'title', 'author', 'category', 'pages', 'price', 'publised_date', 'description']

# class BookSerializer(serializers.Serializer) : --> 구식 방법
    # bid = serializers.IntegerField(primary_key=True) # 책 ID
    # title = serializers.CharField(max_length=50)     # 책 제목
    # author = serializers.CharField(max_length=50)    # 저자 
    # category = serializers.CharField(max_length=50)  # 카테고리
    # pages = serializers.IntegerField()               # 페이지 수
    # price = serializers.IntegerField()               # 가격
    # published_date = serializers.DateField()         # 출판일
    # description = serializers.TextField()            # 도서 설명

    # def create(self, validated_data) :
    #     return Book.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.bid = validated_data.get('bid', instance.bid)
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.category = validated_data.get('category', instance.category)
    #     instance.pages = validated_data.get('pages', instance.pages)
    #     instance.price = validated_data.get('price', instance.price)
    #     instance.published_date = validated_data.get('published_date', instance.published_date)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.save()

    #     return instance

