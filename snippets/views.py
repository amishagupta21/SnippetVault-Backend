# from rest_framework import generics
from .models import Snippets
from .serializers import SnippetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Generic View api call 

# class SnippetListCreateView(generics.ListCreateAPIView):
#       queryset=Snippets.objects.all()
#       serializer_class = SnippetSerializer

# class SnippetSingleDetailView(generics.RetrieveAPIView):
#       queryset=Snippets.objects.all()
#       serializer_class = SnippetSerializer

# APIView api call

class SnippetListView(APIView):
      def get(self,request):
          snippets=Snippets.objects.all()
          serializer=SnippetSerializer(snippets, many=True)
          return Response(serializer.data)
      
      def post(self,request):
          serializer = SnippetSerializer(data = request.data)
          if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
class SnippetDetailView(APIView):
      def get(self,request,pk):
           snippet = Snippets.objects.get(id=pk)
           serializer = SnippetSerializer(snippet)
           return Response(serializer.data)
      
      def put(self,request,pk):
           snippet=Snippets.objects.get(id=pk)
           serializer=SnippetSerializer(snippet,data=request.data)
           if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
           return Response(serializer.errors)
      
      def delete(self,request,pk):
          snippet=Snippets.objects.get(id=pk)
          snippet.delete()
          return Response(status=204)
