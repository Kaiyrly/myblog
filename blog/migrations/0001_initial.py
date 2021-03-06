# Generated by Django 3.2.9 on 2021-11-12 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=100)),
                ('post_date', models.DateTimeField()),
                ('post_text', models.TextField()),
                ('post_image', models.ImageField(upload_to='post_images/')),
            ],
        ),
    ]
