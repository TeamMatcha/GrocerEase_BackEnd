# Generated by Django 4.0.1 on 2022-01-25 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_listitem_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listitem',
            name='categories',
        ),
        migrations.AddField(
            model_name='listitem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listitems', to='app.category'),
        ),
    ]
