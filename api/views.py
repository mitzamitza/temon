from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from monitor.models import Values
from api.serializers import TempSerializer

@api_view(['GET', 'POST', 'DELETE'])
def temp_list(request):
    """
    List all temps, or create a new temp
    """
    if request.method == 'GET':
        values = Values.objects.all()
        serializer = TempSerializer(values, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TempSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def temp_detail(request, pk):
    """
    Get, update or delete a specific temp
    """
    try:
        temp = Values.objects.get(pk=pk)
    except Values.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TempSerializer(temp)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TempSerializer(temp, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        temp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
