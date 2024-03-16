from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from django.contrib.auth import logout
from .models import CustomUser
from .serializers import CustomUserSerializer

class RegisterAPI(generics.GenericAPIView):
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({'user': CustomUserSerializer(user, context=self.get_serializer_context()).data,
                         'token': token})

class LoginAPI(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = (TokenAuthentication,)
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = CustomUser.objects.filter(email=email).first()

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=400)

        if not user.check_password(password):
            return Response({'error': 'Invalid credentials'}, status=400)

        _, token = AuthToken.objects.create(user)
        return Response({'user': CustomUserSerializer(user, context=self.get_serializer_context()).data,
                         'token': token})

class LogoutAPI(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        # Invalidate the user's token
        request.auth.delete()
        # Logout the user
        logout(request)
        return Response({'success': 'Successfully logged out'}, status=200)

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user