from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User as U

# Create your models here.


class PayPlan(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)


# AbstractUser , UserDetail 둘다 사용 가능 AbstractUser 사용시 settings.py에 AUTH_USER_MODEL = "shortener.Users" 추가 필요
class Users(AbstractUser):
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)


class UserDetail(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)