# Generated by Django 2.1.5 on 2019-02-19 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0002_delete_resumetemp'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeTemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_template', models.CharField(max_length=2)),
            ],
        ),
    ]
