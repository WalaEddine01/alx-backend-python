from .serializers import UserSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh, token_verify

class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data.copy()
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user": UserSerializer(user).data,
                "message": "User created successfully."
            }, status=201)

