# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-28 03:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('nid', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe9\xa2\x98')),
                ('summary', models.CharField(max_length=255, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\xae\x80\xe4\xbb\x8b')),
                ('read_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
                ('up_count', models.IntegerField(default=0)),
                ('down_count', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('article_type_id', models.IntegerField(choices=[(1, b'Python'), (2, b'Linux'), (3, b'OpenStack'), (4, b'GoLang')], default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Article2Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Article', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9')),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='repository.Article', verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x96\x87\xe7\xab\xa0')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('nid', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe5\x8d\x9a\xe5\xae\xa2\xe6\xa0\x87\xe9\xa2\x98')),
                ('site', models.CharField(max_length=32, unique=True, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe5\x8d\x9a\xe5\xae\xa2\xe5\x89\x8d\xe7\xbc\x80')),
                ('theme', models.CharField(max_length=32, verbose_name=b'\xe5\x8d\x9a\xe5\xae\xa2\xe4\xb8\xbb\xe9\xa2\x98')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe6\xa0\x87\xe9\xa2\x98')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Blog', verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\x8d\x9a\xe5\xae\xa2')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('nid', models.BigAutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=255, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Article', verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x96\x87\xe7\xab\xa0')),
                ('reply', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='back', to='repository.Comment', verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe8\xaf\x84\xe8\xae\xba')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe\xe5\x90\x8d\xe7\xa7\xb0')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Blog', verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\x8d\x9a\xe5\xae\xa2')),
            ],
        ),
        migrations.CreateModel(
            name='UpDown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up', models.BooleanField(verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe8\xb5\x9e')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Article', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0')),
            ],
        ),
        migrations.CreateModel(
            name='UserFans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('nid', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, unique=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(max_length=64, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('nickname', models.CharField(max_length=32, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('avatar', models.ImageField(upload_to=b'', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('fans', models.ManyToManyField(related_name='f', through='repository.UserFans', to='repository.UserInfo', verbose_name=b'\xe7\xb2\x89\xe4\xb8\x9d\xe4\xbb\xac')),
            ],
        ),
        migrations.AddField(
            model_name='userfans',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='repository.UserInfo', verbose_name=b'\xe7\xb2\x89\xe4\xb8\x9d'),
        ),
        migrations.AddField(
            model_name='userfans',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='repository.UserInfo', verbose_name=b'\xe5\x8d\x9a\xe4\xb8\xbb'),
        ),
        migrations.AddField(
            model_name='updown',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.UserInfo', verbose_name=b'\xe8\xb5\x9e\xe6\x88\x96\xe8\xb8\xa9\xe7\x94\xa8\xe6\x88\xb7'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.UserInfo', verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe8\x80\x85'),
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='repository.UserInfo'),
        ),
        migrations.AddField(
            model_name='article2tag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Tag', verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe'),
        ),
        migrations.AddField(
            model_name='article',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Blog', verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\x8d\x9a\xe5\xae\xa2'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='repository.Category', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(through='repository.Article2Tag', to='repository.Tag'),
        ),
        migrations.AlterUniqueTogether(
            name='userfans',
            unique_together=set([('user', 'follower')]),
        ),
        migrations.AlterUniqueTogether(
            name='updown',
            unique_together=set([('article', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='article2tag',
            unique_together=set([('article', 'tag')]),
        ),
    ]
