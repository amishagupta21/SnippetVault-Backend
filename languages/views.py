from .models import Languages
from .serializers import LanguagesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LanguagesListView(APIView):

    def get(self, request):
        languages = Languages.objects.all()
        serializer = LanguagesSerializer(languages, many=True)
        return Response(serializer.data)
    
    def post(self , request):
        serializer=LanguagesSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LanguageDetailView(APIView):
     def get(self,request,pk):
         language=Languages.objects.get(id=pk)
         serializer=LanguagesSerializer(language)
         return Response(serializer.data)
     
     def put(self,request,pk):
         language=Languages.objects.get(id=pk)
         serializer=LanguagesSerializer(language,data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         return Response(serializer.errors)
     
     def patch(self,request,pk):
         language=Languages.objects.get(id=pk)
         serializer=LanguagesSerializer(language,data=request.data,partial=True)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         return Response(serializer.errors)
            
     
     def delete(self,request,pk):
         language=Languages.objects.get(id=pk)
         language.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
     
    #  language = get_object_or_404(Languages, id=pk) -- If ID doesn’t exist → server crashes ---
    # its good to write this 