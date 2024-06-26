# Generated by Django 5.0.6 on 2024-06-18 10:27

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_birth', models.DateField(blank=True, null=True)),
                ('date_death', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Genre(s) du livre', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="La langue d'origine du livre", max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Ex: Résumé du livre', max_length=1000)),
                ('years', models.DateField()),
                ('isbn', models.CharField(help_text='ISBN de 13 caractères', max_length=13, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.author')),
                ('genre', models.ManyToManyField(help_text='Sélectionnez le genre du livre', to='catalog.genre')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.language')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Numéros unique du livre dans la librairie', primary_key=True, serialize=False)),
                ('date_emprunt', models.DateField()),
                ('date_retour', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'Maintenance'), ('d', 'Disponible'), ('r', 'Réservé')], default='d', help_text='Status du livre ?', max_length=1)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.book')),
            ],
        ),
    ]
