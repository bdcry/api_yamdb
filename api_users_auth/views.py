import uuid

from django.core.mail import send_mail
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import ConfirmationCode, CustomUser
from .permissions import IsAdminRole, IsSuperuser
from .serializers import (ConfirmationCodeSerializer, CustomUserSerializer,
                          MyTokenObtainPairSerializer)


class HttpResponseUnauthorized(HttpResponse):
    def __init__(self):
        self.status_code = 401


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAdminRole | IsSuperuser, IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ('username',)
    lookup_field = 'username'

    @action(detail=False,
            methods=['GET', 'PATCH'],
            permission_classes=(IsAuthenticated,)
            )
    def me(self, request):
        user = self.request.user
        serializer = self.get_serializer(
            user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def get_confirmation_code(request):
    print('request:', request)
    serializer = ConfirmationCodeSerializer(data=request.data)
    print('serializer = ', serializer)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    user_email = serializer.validated_data['email']
    confirmation_code = str(uuid.uuid4())
    if confirmation_code is not None:
        send_mail(
            'Your confirmation code',
            confirmation_code,
            'nemykin.eu@yandex.ru',
            [user_email],
            fail_silently=False,
        )
        ConfirmationCode.objects.create(
            email=user_email,
            confirmation_code=confirmation_code
        )
        return HttpResponse(f"{'Confirmation code was sent to your email'}")
    return HttpResponseUnauthorized()
