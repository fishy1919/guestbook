# Generated by Django 5.0.6 on 2024-07-05 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30, verbose_name='留言者')),
                ('receipt', models.CharField(max_length=60, verbose_name='收件人')),
                ('subject', models.CharField(max_length=128, verbose_name='留言主題')),
                ('content', models.TextField(verbose_name='留言內容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='留言時間')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='最後修改時間')),
            ],
        ),
    ]
