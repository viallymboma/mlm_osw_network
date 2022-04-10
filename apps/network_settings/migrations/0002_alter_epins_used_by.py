# Generated by Django 4.0.3 on 2022-03-31 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps_user_accounts', '0001_initial'),
        ('network_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epins',
            name='used_by',
            field=models.ForeignKey(blank=True, default=0, help_text='Personal volume attached', null=True, on_delete=django.db.models.deletion.CASCADE, to='apps_user_accounts.clientstable'),
        ),
    ]