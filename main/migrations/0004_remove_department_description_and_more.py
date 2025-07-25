# Generated by Django 5.2.1 on 2025-05-29 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_message_content_remove_message_sender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='description',
        ),
        migrations.AddField(
            model_name='department',
            name='detailed_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='short_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
