# Generated by Django 5.0.3 on 2024-03-30 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memory',
            name='status',
            field=models.CharField(choices=[('in progress', 'In progress'), ('planned', 'Planned'), ('archived', 'Archived')], default='planned', max_length=11),
        ),
        migrations.AlterField(
            model_name='picture',
            name='memory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='memory.memory'),
        ),
        migrations.AlterField(
            model_name='post',
            name='memory_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='memory.memory'),
        ),
    ]
