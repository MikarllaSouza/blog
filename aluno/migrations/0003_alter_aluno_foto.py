# Generated by Django 5.1 on 2024-08-29 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0002_aluno_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(blank=True, default=None, upload_to='products/covers/%Y/%m/%d/'),
        ),
    ]
