from pyexpat import model
from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField('회사명', max_length=200)
    country = models.CharField('국가', max_length=200)
    region = models.CharField('지역', max_length=200)
    skills = models.TextField('사용기술')

class Advertisement(models.Model):
    company_id = models.ForeignKey(
        to=Company, 
        verbose_name='회사ID', 
        on_delete=models.CASCADE,
        related_name='ads',
        )
    position = models.CharField('채용포지션', max_length=200)
    signing_bonus = models.IntegerField('채용보상금')
    content = models.TextField('채용내용')
    skills = models.CharField('사용기술', max_length=200)