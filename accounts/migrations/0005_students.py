# Generated by Django 3.2.6 on 2021-08-11 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_institutionsupervisor_universitysupervisor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricNum', models.CharField(max_length=150)),
                ('department', models.CharField(max_length=250)),
                ('regdate', models.DateTimeField(auto_now_add=True)),
                ('duration', models.IntegerField()),
                ('InstitutionSupervisor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.institutionsupervisor')),
                ('universityInspec', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.universitysupervisor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]