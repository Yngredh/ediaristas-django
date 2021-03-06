# Generated by Django 3.2 on 2021-06-17 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diarista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('telefone', models.CharField(max_length=11)),
                ('logradouro', models.CharField(max_length=60)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=100)),
                ('complemento', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=2)),
                ('estado', models.CharField(max_length=2)),
                ('codigo_ibge', models.IntegerField()),
                ('foto_usuario', models.ImageField(upload_to='')),
            ],
        ),
    ]
