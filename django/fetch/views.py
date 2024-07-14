from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from django.forms.models import model_to_dict
import logging

from admin_page.models import Details, Health, Sensors

logger = logging.getLogger(__name__)

def returnValue(table, user_id):
    if table.lower() == 'details':
        table = Details
    elif table.lower() == 'health':
        table = Health
    elif table.lower() == 'sensors':
        table = Sensors

    try:
        data = table.objects.filter(user_id=user_id).order_by('-created_time').first()
        return model_to_dict(data)
    except:
        return None

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def TableView(request, table):
    if request.method == 'POST':
        user = request.user
        logger.error(f'User {user.id} requested {table} Table.')

        fromDB = returnValue(table, user.id)
        if fromDB:
            return Response(fromDB, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Data not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)