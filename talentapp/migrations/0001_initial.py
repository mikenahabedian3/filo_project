# Generated by Django 4.2.5 on 2023-09-21 22:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('resume', models.TextField()),
                ('status', models.CharField(choices=[('Applied', 'Applied'), ('Interviewed', 'Interviewed'), ('Rejected', 'Rejected'), ('Hired', 'Hired')], default='Applied', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ParentOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talentapp.company')),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('is_used', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talentapp.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talentapp.company')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='parent_organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talentapp.parentorganization'),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.TextField()),
                ('date_applied', models.DateTimeField(auto_now_add=True)),
                ('review', models.TextField(blank=True)),
                ('is_hired', models.BooleanField(default=False)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talentapp.candidate')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talentapp.job')),
            ],
        ),
    ]