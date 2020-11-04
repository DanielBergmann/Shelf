from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BookAuthor, BookObject
from .serializers import BookSerializer, BookAuthorSerializer


class BookView(APIView):
	def get(self, request):
		books = BookObject.objects.all()
		serializer = BookSerializer(books, many=True)
		return Response({"books": serializer.data})

class BookAuthorsView(APIView):

	def get(self, request):
		authors = BookAuthor.objects.all()
		serializer = BookAuthorSerializer(authors, many=True)
		return Response({'book_authors': serializer.data})
