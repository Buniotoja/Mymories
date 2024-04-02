# Generated by Django 5.0.3 on 2024-03-29 10:54

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('date', models.DateTimeField()),
                ('latitude', models.FloatField(default=0, max_length=8)),
                ('longitude', models.FloatField(default=0, max_length=8)),
                ('memory_type', models.CharField(choices=[('standard', 'Standard coming outdoor'), ('adventure', 'Crazy trip to interested place'), ('travel', 'Some days travelling'), ('celebration', 'Birthday or something like that')], default='standard', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='pictures/%Y/%m')),
                ('memory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memory.memory')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('text', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('memory_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memory.memory')),
                ('picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memory.picture')),
            ],
        ),
    ]