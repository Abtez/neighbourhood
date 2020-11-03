# Generated by Django 3.1.2 on 2020-11-03 19:40

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(max_length=120)),
                ('avatar', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('title', models.CharField(max_length=120, null=True)),
                ('content', models.TextField(max_length=1000, null=True, verbose_name='project Description')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_profile', to='neighbour.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('neighbourhood_name', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=120)),
                ('population', models.AutoField(primary_key=True, serialize=False)),
                ('admin', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='admin_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('business_email', models.EmailField(max_length=254)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbour.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_user', to='neighbour.profile')),
            ],
        ),
    ]
