# Generated by Django 4.0.5 on 2022-06-15 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='Date_publication',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Bloguer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bio', models.TextField(max_length=120)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='id_bloguer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.bloguer'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='id_bloguer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.bloguer'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
