from django.shortcuts import render
import json
from django.views import View
from django.http  import JsonResponse
from .models      import Users
from .utils import login_decorator
from config.settings import SECRET_KEY

import bcrypt
import jwt


class SignUp(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            if '' in data['userid'] :
                Users(
                    name     = data['name'],
                    userid       = data['userid'],
                    password    = bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
                ).save()
            return JsonResponse({'message':'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message':'key wrong'}, status=400)


class SignIn(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if Users.objects.filter(userid = data['userid']):
                user = Users.objects.get(userid = data['userid'])
            else:
                return JsonResponse({'message':'id not find'}, status = 401)

            if bcrypt.checkpw(data['password'].encode('utf-8'),user.password.encode('utf-8')) != True:
                return JsonResponse({'message':'password not same'}, status = 401)

            access_token = jwt.encode({'userid':user.id},SECRET_KEY,algorithm='HS256').decode('utf-8')

            return JsonResponse({'message':'login_SUCCESS',"access_token":access_token}, status=200)
        except KeyError:
            return JsonResponse({'message':'key wrong'}, status=400)
