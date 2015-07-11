from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.models import Author, Publisher, Book
from ws.serializers import AuthorSerializer, PublisherSerializer, BookSerializer
import datetime

@api_view(['POST'])
def sync(request, format=None):
    lastSyncDate = None
    try:
        lastSyncDate = datetime.datetime.strptime(request.data['lastSyncDate'], '%Y-%m-%dT%H:%M:%S.%f')
    except:
        pass

    try:
        author_serializer = AuthorSerializer(Author.objects.all(), data=request.data['authors'], many=True)
    
        if author_serializer.is_valid():
            author_serializer.save()
        else:
            return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        pass
    
    try:
        publisher_serializer = PublisherSerializer(Publisher.objects.all(), data=request.data['publishers'], many=True)
    
        if publisher_serializer.is_valid():
            publisher_serializer.save()
        else:
             return Response(publisher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        pass

    try:
        book_serializer = BookSerializer(Book.objects.all(), data=request.data['books'], many=True)
    
        if book_serializer.is_valid():
            book_serializer.save()
        else:
            return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        pass

    if lastSyncDate == None:
        authors = Author.objects.all()
        publishers = Publisher.objects.all()
        books = Book.objects.all()
    else:
        authors = Author.objects.filter(last_change_date__gt=lastSyncDate)
        publishers = Publisher.objects.filter(last_change_date__gt=lastSyncDate)
        books = Book.objects.filter(last_change_date__gt=lastSyncDate)

    author_serializer = AuthorSerializer(authors, many=True)
    publisher_serializer = PublisherSerializer(publishers, many=True)
    book_serializer = BookSerializer(books, many=True)

    return Response({
        'serverDate': datetime.datetime.now(),
        'authors': author_serializer.data,
        'publishers': publisher_serializer.data,
        'books': book_serializer.data
    })

