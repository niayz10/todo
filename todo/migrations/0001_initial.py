# Generated by Django 5.1.4 on 2024-12-13 16:46

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(default='')),
                ('todo_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(default='')),
                ('item_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.todo')),
            ],
        ),
    ]
