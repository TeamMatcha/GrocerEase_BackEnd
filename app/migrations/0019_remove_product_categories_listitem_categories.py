# Generated by Django 4.0.1 on 2022-01-24 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_listitem_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.AddField(
            model_name='listitem',
            name='categories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='app.category'),
            preserve_default=False,
        ),
    ]
