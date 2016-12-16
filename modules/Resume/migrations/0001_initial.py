# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-15 23:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Session', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id_resume', models.AutoField(primary_key=True, serialize=False)),
                ('original_text', models.TextField(default='')),
                ('resume_text', models.TextField(default='')),
                ('key_words', models.TextField(default='')),
                ('id_session', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Session.Session')),
            ],
        ),
    ]