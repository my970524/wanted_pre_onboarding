from turtle import ondrag
from django.db import models

from recruit.models import Advertisement
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Application(models.Model):
    applicant = models.ForeignKey(
        to=User,
        verbose_name='지원자',
        on_delete=models.CASCADE,
        related_name='applications'
    )
    ad = models.ForeignKey(
        to=Advertisement,
        verbose_name='채용공고',
        on_delete=models.CASCADE,
        related_name='applications'
    )