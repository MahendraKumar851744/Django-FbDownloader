from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from tkinter.ttk import *
from requests import get, HTTPError, ConnectionError
from re import findall
from urllib.parse import unquote


class userlist(APIView):
    def get_FB_downloadlink(self,url):

        url = url.replace("www", "mbasic")
        try:
            r = get(url, timeout=5, allow_redirects=True)
            if r.status_code != 200:
                raise HTTPError
            a = findall("/video_redirect/", r.text)
            if len(a) == 0:
                print("[!] Video Not Found...")
                exit(0)
            else:
                return unquote(r.text.split("?src=")[1].split('"')[0])
        except (HTTPError, ConnectionError):
            print("[x] Invalid URL")
            exit(1)

    def post(self, request):
        serializer = userserializer(data=request.data)
        if serializer.is_valid():
            url = serializer.data['url']
            link = ''
            if not "www.facebook.com" in url:
                print("Error")
            else:
                 link= self.get_FB_downloadlink(url)
            data = {'url': link}
            serializer2 = userserializer(data=data)
            if serializer2.is_valid():
                return Response(serializer2.data, status=status.HTTP_201_CREATED)



        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        link = self.get_FB_downloadlink("https://www.facebook.com/groups/181416939015034/permalink/1197267414096643/?ref=share&mibextid=NnVzG8")
        print(link)
        data = {'url': link }
        serializer2 = userserializer(data=data)
        if serializer2.is_valid():
            return Response(serializer2.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
