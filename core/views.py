from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from core.serializers import *

class RegisterView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer

    def post(self,request):
        serializers = Userserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'Adicionado com sucesso'})
        return Response({'Erro ao adicionar usuario'})

class LogoutView(APIView):
    def get(self,request,format=None):
        request.user.auth_token.delete()
        return Response(status = status.HTTP_101_SWITCHING_PROTOCOLS)