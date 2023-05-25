# Generated by Django 4.1.7 on 2023-05-25 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authlibrary', '0001_initial'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowedbook',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowing_user_set', to='book.book'),
        ),
        migrations.AlterField(
            model_name='borrowedbook',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowedbook_set', to='authlibrary.client'),
        ),
    ]