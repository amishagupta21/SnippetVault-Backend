from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tags
from .serializers import TagsSerializers

class TagsListView(APIView):
      def get(self,request):
          tags=Tags.objects.all()
          serializer=TagsSerializers(tags,many=True)
          return Response(serializer.data)
      
      def post(self,request):
           serializer=TagsSerializers(data=request.data)
           if serializer.is_valid():
              serializer.save()
              return Response(serializer.data,status=status.HTTP_201_CREATED)
           return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
class TagsDetailsView(APIView):
     def get(self,request,pk):
          tags=Tags.objects.get(id=pk)
          serializer=TagsSerializers(tags)
          return Response(serializer.data)
     
     def put(self,request,pk):
          tags=Tags.objects.get(id=pk)
          serializer=TagsSerializers(tags,data=request.data)
          if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
          return Response(serializer.errors)
         
     def delete(self,request,pk):
          tags=Tags.objects.get(id=pk)
          tags.delete()
          return Response(status=204)
        

