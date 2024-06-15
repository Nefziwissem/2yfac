# Generated by Django 4.2.7 on 2024-04-28 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rembourssement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, help_text='Indicates whether the rembourssement is active or not.')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('authorization_number', models.CharField(max_length=255, null=True, unique=True, verbose_name='Authorization Number')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, null=True, unique=True, verbose_name='Amount')),
                ('merchant_number', models.CharField(max_length=255, null=True, verbose_name='Merchant Number')),
                ('merchant_email', models.EmailField(max_length=254, null=True, unique=True, verbose_name='Merchant Email')),
                ('merchant_name', models.CharField(max_length=255, null=True, verbose_name='Merchant Name')),
                ('status', models.CharField(choices=[('created', 'Created'), ('sent_to_merchant', 'Sent to Merchant'), ('processing_by_paymee', 'Processing by Paymee'), ('processing_by_bank', 'Processing by Bank'), ('won', 'Won'), ('lost', 'Lost'), ('cancelled', 'Cancelled'), ('reactivate', 'Reactivate')], max_length=100, null=True, verbose_name='Status')),
                ('reason', models.TextField(null=True, verbose_name='Reason')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Date')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Modification Date')),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_rembourssements', to=settings.AUTH_USER_MODEL, verbose_name='Assigned To')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_rembourssements', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Rembourssement',
                'verbose_name_plural': 'Rembourssement',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('rembourssement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='rembourssement.rembourssement')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rembourssement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentss', to='rembourssement.rembourssement')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentss', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ActionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rembourssement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log', to='rembourssement.rembourssement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_log', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
