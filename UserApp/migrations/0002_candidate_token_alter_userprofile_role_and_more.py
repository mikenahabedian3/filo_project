# Generated by Django 4.2.5 on 2023-09-22 01:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.TextField()),
                ('status', models.CharField(choices=[('Applied', 'Applied'), ('Interviewed', 'Interviewed'), ('Rejected', 'Rejected'), ('Hired', 'Hired')], default='Applied', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('is_used', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.candidate')),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='UniqueLink',
        ),
    ]