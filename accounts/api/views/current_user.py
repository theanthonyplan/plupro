from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes
from rest_framework.response import Response
from ..auth import CsrfExemptSessionAuthentication
from ..serializers import UserSerializer

@api_view(['GET'])
@authentication_classes([CsrfExemptSessionAuthentication])
def current_user(request):
	if hasattr(request, 'user') and request.user.is_authenticated:
		data = UserSerializer(request.user).data
		return Response(data)

	return Response({})
