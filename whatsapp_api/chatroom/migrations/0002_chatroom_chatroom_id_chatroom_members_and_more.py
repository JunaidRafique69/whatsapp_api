# Generated by Django 4.2.7 on 2023-12-04 08:45

from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='chatroom_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='max_members',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
