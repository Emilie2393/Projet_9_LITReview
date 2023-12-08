# Generated by Django 4.2.7 on 2023-12-04 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='BookblogUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contribution', models.CharField(blank=True, max_length=255)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookblog.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'blog')},
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='users',
            field=models.ManyToManyField(related_name='contribution', through='bookblog.BookblogUsers', to=settings.AUTH_USER_MODEL),
        ),
    ]
