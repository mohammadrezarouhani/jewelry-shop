# Generated by Django 4.0.4 on 2022-05-04 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=55)),
                ('type', models.CharField(choices=[['coin', 1], ['jewelry', 2], ['gold_bullion', 3]], max_length=55)),
                ('weight', models.FloatField(default=0.0)),
                ('unit', models.CharField(choices=[['ons', 1], ['methghal', 2], ['geram', 3]], max_length=15)),
                ('date', models.DateField(verbose_name=django.utils.timezone.now)),
                ('image', models.ImageField(default='def.jpg', upload_to='product_image')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]