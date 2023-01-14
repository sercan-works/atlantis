from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
import json
from django.core.serializers import serialize
from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework.response import Response

# class RegisterSerializer(serializers.ModelSerializer):
    
#     email = serializers.EmailField(
#         required = True,
#         validators = [validators.UniqueValidator(queryset=User.objects.all())]
#     )
#     password = serializers.CharField(
#         write_only = True,
#         required = True,
#         validators = [validate_password],
#         style = {"input_type" : "password"}
#     )
#     password2 = serializers.CharField(
#         write_only = True,
#         required = True,
#         style = {"input_type" : "password"}
#     )
    
    
#     class Meta:
#         model = User
#         fields = [            
#             #'username',
#             #'first_name',
#             #'last_name',
#             'email',
#             'password',
#             'password2'
#         ]
#         extra_kwargs = {
#             'password': {'write_only' : True},
#             'password2': {'write_only' : True},
#         }

#     def create(self, validated_data):
#         password = validated_data.get('password')
#         validated_data.pop("password2")
#         user = User.objects.create(**validated_data)
#         user.set_password(password)
#         user.save()
#         return user
        
#     def validate(self, data):
#         if data["password"] != data["password2"]:
#             raise serializers.ValidationError(
#                 {"password" : "Password fields didn't match."}
#             )
#         return data



class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    first_name = serializers.CharField(required=False, write_only=True)
    last_name = serializers.CharField(required=False, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    ("Bu mail adresi kullanılıyor."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                ("Girilen paralolar uyumsuz."))
        return data

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user
    
    
class UserTokenSerializer(serializers.ModelSerializer):
    #email = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email","is_staff")

    # def get_email(self,obj):
    #     return obj
 
class CustomTokenSerializer(TokenSerializer):
     
     user = UserTokenSerializer(read_only = True) 
     class Meta(TokenSerializer.Meta):
         fields = ("key", "user")
         
class StaffCheckSerializer(serializers.ModelSerializer):
    # staff_user = serializers.SerializerMethodField()

    class Meta:
        model=User
        fields = ['is_staff']

