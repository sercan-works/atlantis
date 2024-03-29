# Generated by Django 4.1.6 on 2023-03-28 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('envanter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pc', to='envanter.cpu')),
                ('kasa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pc', to='envanter.kasa')),
                ('motherboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pc', to='envanter.motherboard')),
                ('psu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pc', to='envanter.psu')),
                ('ram', models.ManyToManyField(blank=True, null=True, to='envanter.ram')),
            ],
        ),
    ]
