from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import bcrypt
import re
# Create your models here.

EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def isValidRegistration(self, userInfo, request):
        passFlag = True
        if not userInfo['first_name'].isalpha():
            passFlag = False
        if len(userInfo['first_name']) < 2:
            passFlag = False
        if not userInfo['last_name'].isalpha():
            passFlag = False
        if len(userInfo['last_name']) < 2:
            passFlag = False
        if not EMAIL_REGEX.match(userInfo['email']):
            passFlag = False
        if len(userInfo['password']) < 7:
            passFlag = False
        if userInfo['password'] != userInfo['confirm_password']:
            passFlag = False
        if User.objects.filter(email = userInfo['email']):
			passFlag = False

        if passFlag:
            if User.userManager.all:
                status = 1
                hashed = bcrypt.hashpw(userInfo['password'].encode(), bcrypt.gensalt())
                self.create(first_name = userInfo['first_name'], last_name = userInfo['last_name'], email = userInfo['email'], password = hashed, status=status)
            else:
                status = 9
                hashed = bcrypt.hashpw(userInfo['password'].encode(), bcrypt.gensalt())
                self.create(first_name = userInfo['first_name'], last_name = userInfo['last_name'], email = userInfo['email'], password = hashed, status=status)
        else:
            messages.error(request, "Invalid Registration. Please try again.")
        return passFlag

    def UserExistsLogin(self, userInfo, request):
        passFlag = True
        if User.objects.filter(email = userInfo['email']):
            hashed = User.objects.get(email = userInfo['email']).password
            hashed = hashed.encode('utf-8')
            password = userInfo['password']
            password = password.encode('utf-8')
            if bcrypt.hashpw(password, hashed) == hashed:
                passFlag = True
            else:
                passFlag = False
        else:
            messages.warning(request, "Unsuccessful login.")
            passFlag = False
        return passFlag


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    status = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()
    objects = models.Manager()
