import jwt                                                
import json                 
import requests

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from config.DBconnent import SECRET_KEY
from .models import Users

def login_decorator(func):
    def wrapper(self,request,*args, **kwargs):
        if "Authorization" not in request.headers:
            return JsonResponse({"message":"INALID_LOGIN"},status=401)
        token = request.headers["Authorization"]
        try:
            user_token = jwt.decode(token,SECRET_KEY,algorithm='HS256')
            user = Users.objects.get(id=user_token["userid"])
            request.user = user
        except jwt.DecodeError:
            return JsonResponse({"message":"INVALID TOKEN"},status=401)
        except User.DoesNotExist:
            return JsonResponse({"message":"NOT EXITST USER"},status=401)
        return func(self,request, *args, **kwargs)
    return wrapper