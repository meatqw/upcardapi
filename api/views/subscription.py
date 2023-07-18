from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import *
from api.serializers import *


class SubscriptionAPIView(APIView):
    """Получить все подписки по токену пользвоателя"""

    def get(self, request):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

