# Generated by Django 4.0.1 on 2022-01-20 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_listitem_remove_list_items_delete_item_listitem_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listitem',
            name='item',
        ),
        migrations.AddField(
            model_name='listitem',
            name='list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list', to='app.list'),
        ),
    ]
