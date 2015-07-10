from rest_framework import serializers
from books.models import Author, Publisher, Book

class PublisherListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        publisher_mapping = {publisher.id: publisher for publisher in instance}
        data_mapping = {item['id']: item for item in validated_data}

        ret = []

        for publisher_id, data in data_mapping.items():
            publisher = publisher_mapping.get(publisher_id, None)
            if publisher is None:
                data['id'] = None;
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(publisher, data))

        return ret

class PublisherSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Publisher
        fields = ('id', 'name')
        list_serializer_class = PublisherListSerializer


class AuthorListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        author_mapping = {author.id: author for author in instance}
        data_mapping = {item['id']: item for item in validated_data}

        ret = []

        for author_id, data in data_mapping.items():
            author = author_mapping.get(author_id, None)
            if author is None:
                data['id'] = None;
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(author, data))

        return ret

class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Author
        fields = ('id', 'name')
        list_serializer_class = AuthorListSerializer


class BookListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        book_mapping = {book.id: book for book in instance}
        data_mapping = {item['id']: item for item in validated_data}

        ret = []

        for book_id, data in data_mapping.items():
            book = book_mapping.get(book_id, None)
            if book is None:
                data['id'] = None;
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(book, data))

        return ret

class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Book
        fields = ('id', 'authors', 'publisher', 'title', 'description')
        list_serializer_class = BookListSerializer

