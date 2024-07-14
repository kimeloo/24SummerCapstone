from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from django.forms.models import model_to_dict
from datetime import datetime, timedelta
import logging

from admin_page.models import Details, Health, Sensors

logger = logging.getLogger(__name__)

def toTable(table):
    if table.lower() == 'details':
        return Details
    elif table.lower() == 'health':
        return Health
    elif table.lower() == 'sensors':
        return Sensors
    else:
        return None

def returnValue(table, user_id):
    Table = toTable(table)

    try:
        data = Table.objects.filter(user_id=user_id).order_by('-created_time').first()
        return model_to_dict(data)
    except:
        return None

def InsertOrUpdate(table, user_id, data):
    Table = toTable(table)
    data = dict(data)
    for key in data:
        if type(data[key])==list:
            data[key] = ', '.join(data[key])
    try:
        latest = Table.objects.filter(user_id=user_id).order_by('-created_time').first()
        if latest:
            print("OK")
            print(latest.created_time)
            print(datetime.now())
            latestTime = datetime.fromisoformat(str(latest.created_time)[:19])
            currentTime = datetime.fromisoformat(str(datetime.now())[:19])
            timeDiff = currentTime - latestTime
            if timeDiff <= timedelta(hours=2):
                latest.__dict__.update(**data)
                latest.save()
                return True
        Table.objects.create(user_id=user_id, **data)
        return True
    except:
        return False

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

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def TableInsert(request, table):
    if request.method == 'POST':
        user = request.user
        logger.error(f'User {user.id} requested to insert data.')
        if InsertOrUpdate(table, user.id, request.data):
            return Response({'success': 'Data inserted successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Data not inserted'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
