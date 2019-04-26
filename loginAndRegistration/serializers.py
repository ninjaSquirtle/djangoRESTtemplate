from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedIdentityField
from .models import User

class UserSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name="login:user-detail")
    class Meta:
        model = User
        fields = ('url', 'id', 'email', 'api_key')