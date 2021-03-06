# Generated by Django 3.2.13 on 2022-06-21 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recruit', '0003_rename_name_company_company_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='recruit.advertisement', verbose_name='채용공고')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL, verbose_name='지원자')),
            ],
        ),
    ]
