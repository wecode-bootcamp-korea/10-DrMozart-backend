import re
import jwt
import json
import bcrypt

from .models      import Users
from config.DBConnent    import EMAIL
from .text import message
from config.DBConnent import SECRET_KEY

from django.views import View
from django.http  import JsonResponse
from django.core.exceptions import ValidationError

from django.shortcuts       import redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http              import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail               import EmailMessage
from django.utils.encoding          import force_bytes, force_text

class GoogleLogin(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            email = data["user"]
            name = data["name"]
            try:
                user = Users.objects.get(user=email)
            except Users.DoesNotExist:
                user = Users.objects.create(
                    user    = data['user'],
                    email = data['user'],
                    name = data["name"],
                    is_active = True,
                    login_method=Users.LOGIN_GOOGLE,
                )
            access_token = jwt.encode({'user':user.id},SECRET_KEY,algorithm='HS256').decode('utf-8')
            return JsonResponse({'message':'SUCCESS',"access_token":access_token}, status=200)
            
        except KeyError:
            return JsonResponse({'message':'INVALID_DATA'}, status=401)

class SignUp(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if re.search("[^a-zA-Z0-9]{6,12}$",data['user']):
                return JsonResponse({'message':'id check'}, status=400)
            elif re.search(r"[^A-Za-z0-9!@#$]{6,12}$",data['password']):
                return JsonResponse({'message':'password check'}, status=400)
            else:
                try:
                    Users.objects.get(user=data['user'])
                    return JsonResponse({'message':'EXISTS ID'}, status=401)
                except Users.DoesNotExist:
                    user = Users.objects.create(
                        user    = data['user'],
                        email = data['email'],
                        password  = bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt()).decode('utf-8'),
                        is_active = False
                    )
                    
                    current_site = get_current_site(request)
                    domain = current_site.domain
                    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                    token = jwt.encode({'user':user.id},SECRET_KEY,algorithm='HS256').decode('utf-8')
                    message_data = message(domain, uidb64, token)

                    mail_title = "이메일 인증을 완료해주세요"
                    mail_to = data['email']
                    email = EmailMessage(mail_title, message_data, to=[mail_to])
                    email.send()

                return JsonResponse({'message':'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'message':'key wrong'}, status=402)
        except TypeError:
            return JsonResponse({'message':'type wrong'}, status=403)
        except ValidationError:
            return JsonResponse({'message':'VALIDATION_ERROR'}, status=404)

class SignIn(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if Users.objects.filter(user = data['user']):
                user = Users.objects.get(user = data['user'])
            else:
                return JsonResponse({'message':'id not find'}, status = 402)

            if bcrypt.checkpw(data['password'].encode('utf-8'),user.password.encode('utf-8')) != True:
                return JsonResponse({'message':'password not same'}, status = 401)

            access_token = jwt.encode({'user':user.id},SECRET_KEY,algorithm='HS256').decode('utf-8')

            return JsonResponse({'message':'login_SUCCESS',"access_token":access_token}, status=200)
        except KeyError:
            return JsonResponse({'message':'key wrong'}, status=400)

class Activate(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = Users.objects.get(pk=uid)
            user_dic = jwt.decode(token,SECRET_KEY,algorithm='HS256')
            if user.id == user_dic["user"]:
                user.is_active = True
                user.save()
                return redirect("http://10.58.5.40:3000/signin")

            return JsonResponse({'message':'auth fail'}, status=400)
        except ValidationError:
            return JsonResponse({'message':'type_error'}, status=400)
        except KeyError:
            return JsonResponse({'message':'INVALID_KEY'}, status=400)

