# Generated by Django 4.0.3 on 2023-02-05 16:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_user_data_twitter_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]