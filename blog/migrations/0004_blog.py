# Generated by Django 5.1.2 on 2024-11-01 10:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_capa'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=2000)),
                ('logo', models.ImageField(upload_to='')),
                ('instagram', models.URLField()),
                ('facebook', models.URLField()),
                ('github', models.URLField()),
                ('autores', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]