from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from django.forms.models import model_to_dict
from datetime import datetime, timedelta
import logging

from admin_page.models import Details, Health, Sensors, Recommend
from static import rm0708

logger = logging.getLogger(__name__)

def toTable(table):
    if table.lower() == 'details':
        return Details
    elif table.lower() == 'health':
        return Health
    elif table.lower() == 'sensors':
        return Sensors
    elif table.lower() == 'recommend':
        return Recommend
    else:
        return None

def returnValue(table, user):
    Table = toTable(table)

    try:
        data = Table.objects.filter(user=user).order_by('-created_time').first()
        return model_to_dict(data)
    except:
        return None

def InsertOrUpdate(table, user, data):
    Table = toTable(table)
    data = dict(data)
    for key in data:
        if type(data[key])==list:
            data[key] = ', '.join(data[key])
    try:
        latest = Table.objects.filter(user=user).order_by('-created_time').first()
        if latest:
            latestTime = datetime.fromisoformat(str(latest.created_time)[:19])
            currentTime = datetime.fromisoformat(str(datetime.now())[:19])
            timeDiff = currentTime - latestTime
            if timeDiff <= timedelta(hours=2):
                latest.__dict__.update(**data)
                latest.save()
                return True
    except:
        pass
    Table.objects.create(user=user, **data)
    return True

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def TableView(request, table):
    if request.method == 'POST':
        user = request.user
        logger.info(f'User {user.id} requested {table} Table.')

        fromDB = returnValue(table, user)
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
        logger.info(f'User {user.id} requested to insert data.')
        if InsertOrUpdate(table, user, request.data):
            logger.error(user.id)
            returnList = rm0708.main(user_id=user.id)
            # returnList = ['(TEST 문구) ㅇㅇㅇ 항목의 수치 관리가 필요합니다.']
            return Response({'success': 'Data inserted successfully', 'returnList': returnList}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Data not inserted'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
