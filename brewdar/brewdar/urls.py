from django.conf.urls import patterns, include, url

# admin interface
from django.contrib import admin
admin.autodiscover()

# django rest framework
from users.models import User, Device
from rest_framework import routers, serializers, viewsets


# user
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# device
class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'device_id', 'name', 'verification_token', 'verified',
                  'authentication_token', 'authenticated', 'user']


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


# routes
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'devices', DeviceViewSet)

urlpatterns = patterns('',
    url(r'^', include('users.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
