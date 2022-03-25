from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ShortenerSerializer
from .models import Shortener

@api_view(['GET'])
def getUrl(request, url):
    try:
        # return the shortened url
        shortener = Shortener.objects.filter(short_url=url).first()
        return Response(shortener.long_url)
    except:
        # if URL not valid, return 404
        return Response("No such URL exists", status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def addUrl(request):
    data = request.body.decode("utf-8") 
    # check if shortener instance exists
    shorteners = Shortener.objects.filter(long_url=data)
    if shorteners.exists():
        # if exist, return data
        serializer = ShortenerSerializer(shorteners.first(), many=False)
        return Response(serializer.data)

    # create shortener instance
    shortener = Shortener(long_url=data, short_url=str(abs(hash(data)))[:5])

    try:
        # save to db
        shortener.full_clean()
        shortener.save()
    except ValidationError as e:
        # if invalid, return 400 status code
        print(e)
        return Response(data + " is invalid.", status=status.HTTP_400_BAD_REQUEST)

    serializer = ShortenerSerializer(shortener, many=False)
    return Response(serializer.data)
