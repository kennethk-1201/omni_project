from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ValidationError

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ShortenerSerializer
from .models import Shortener

@api_view(['GET'])
def getUrl(request, url):
    try:
        # return the shortened url
        shortener = Shortener.objects.get(short_url=url)            
        serializer = ShortenerSerializer(shortener, many=False)
        return Response(serializer.data)
    except:
        # if URL not valid, return 404
        return Response("No such URL exists", status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def addUrl(request):
    # check if shortener instance exists
    shortener = Shortener.objects.all().filter(short_url=request.data)
    print(shortener)

    if shortener.exists():
        serializer = ShortenerSerializer(shortener[0], many=False)
        return Response(serializer.data)

    # create shortener instance
    shortener = Shortener(long_url=request.data, short_url=str(abs(hash(request.data)))[:15])

    try:
        # save to db
        shortener.full_clean()
        shortener.save()
    except ValidationError as e:
        # if invalid, return 400 status code
        return Response(e, status=status.HTTP_400_BAD_REQUEST)

    serializer = ShortenerSerializer(shortener, many=False)
    return Response(serializer.data)
