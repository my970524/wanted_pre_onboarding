# Generated by Django 3.2.13 on 2022-06-18 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200, verbose_name='회사명')),
                ('country', models.CharField(max_length=200, verbose_name='국가')),
                ('region', models.CharField(max_length=200, verbose_name='지역')),
                ('skills', models.TextField(verbose_name='사용기술')),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200, verbose_name='채용포지션')),
                ('signing_bonus', models.IntegerField(verbose_name='채용보상금')),
                ('content', models.TextField(verbose_name='채용내용')),
                ('skills', models.CharField(max_length=200, verbose_name='사용기술')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='recruit.company', verbose_name='회사ID')),
            ],
        ),
    ]
