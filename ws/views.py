from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.models import Author, Publisher, Book
from ws.serializers import AuthorSerializer, PublisherSerializer, BookSerializer

@api_view(['POST'])
def sync(request, format=None):
    try:
        author_serializer = AuthorSerializer(Author.objects.all(), data=request.data['authors'], many=True)
        publisher_serializer = PublisherSerializer(Publisher.objects.all(), data=request.data['publishers'], many=True)
        book_serializer = BookSerializer(Book.objects.all(), data=request.data['books'], many=True)
    
        if author_serializer.is_valid() and publisher_serializer.is_valid() and book_serializer.is_valid():
            author_serializer.save()
            publisher_serializer.save()
            book_serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        pass

    author_serializer = AuthorSerializer(Author.objects.all(), many=True)
    publisher_serializer = PublisherSerializer(Publisher.objects.all(), many=True)
    book_serializer = BookSerializer(Book.objects.all(), many=True)

    return Response({
        'authors': author_serializer.data,
        'publishers': publisher_serializer.data,
        'books': book_serializer.data
    })

